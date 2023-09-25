import os
import shutil
import asyncio

from input_processing_actions import (
    read_path,
    validate_folder_path,
    read_validate_synchronization_interval,
)

from hashing_content import hash_folder_files

print("Welcome to the Folder Synchronizer app!", "\n")

prompt_source_folder = "The path of the source folder: "
prompt_replica_folder = "The path of the replica folder: "
prompt_log_file = (
    "The path of the log file (will be created automatically if it doesn't exist): "
)

os_independent_path_source_folder: str = read_path(prompt_source_folder)
validate_folder_path(os_independent_path_source_folder)

os_independent_path_replica_folder: str = read_path(prompt_replica_folder)
validate_folder_path(os_independent_path_replica_folder)

os_independent_path_log_file = read_path(prompt_log_file)

synchronization_interval: float = read_validate_synchronization_interval()


async def project_source_into_replica_folder(
    path_source_folder: str, path_replica_folder: str, path_log_file: str
):
    directory_paths_source, paths_hashes_files_source = hash_folder_files(
        path_source_folder
    )

    for directory_path in directory_paths_source:
        path_subdirectory_replica = directory_path.replace(
            path_source_folder, path_replica_folder
        )
        os.makedirs(path_subdirectory_replica, exist_ok=True)

    _, paths_hashes_files_replica = hash_folder_files(path_replica_folder)

    for (
        path_file_source,
        hashed_file_source,
    ) in paths_hashes_files_source.items():
        relative_path_source_file = os.path.relpath(
            path_file_source, path_source_folder
        )

        to_be_path_file_replica = os.path.join(
            path_replica_folder, relative_path_source_file
        )

        if not os.path.isfile(to_be_path_file_replica):
            included_count_source = 0
            included_count_replica = 0
            subpaths_source = []
            for path_file, hashed_file in paths_hashes_files_source.items():
                relative_path_file = os.path.relpath(path_file, path_source_folder)
                if (
                    os.path.dirname(relative_path_file)
                    == os.path.dirname(relative_path_source_file)
                    and hashed_file == hashed_file_source
                ):
                    subpaths_source.append(path_file)
                    included_count_source += 1

            for path_file, hashed_file in paths_hashes_files_replica.items():
                relative_path_file = os.path.relpath(path_file, path_replica_folder)
                if (
                    os.path.dirname(relative_path_file)
                    == os.path.dirname(relative_path_source_file)
                    and hashed_file == hashed_file_source
                ):
                    included_count_replica += 1

            for _ in range(included_count_source - included_count_replica):
                reporting_pattern = f"CPY FILE {path_file_source} IN DIR {os.path.dirname(to_be_path_file_replica)}"
                print(reporting_pattern, "\n")

                shutil.copy2(path_file_source, os.path.dirname(to_be_path_file_replica))

                with open(path_log_file, "a") as file:
                    file.write(reporting_pattern + "\n")

            _, paths_hashes_files = hash_folder_files(path_replica_folder)

            subpaths_replica = []
            for path_file, hashed_file in paths_hashes_files.items():
                relative_path_file = os.path.relpath(path_file, path_replica_folder)
                if (
                    os.path.dirname(relative_path_file)
                    == os.path.dirname(relative_path_source_file)
                    and hashed_file == hashed_file_source
                ):
                    subpaths_replica.append(path_file)

            for index in range(len(subpaths_replica)):
                renaming_path = os.path.join(
                    os.path.dirname(subpaths_replica[index]),
                    os.path.basename(subpaths_source[index]),
                )
                os.rename(subpaths_replica[index], renaming_path)


async def synchronize_periodically(synchronization_interval: float) -> None:
    while True:
        await project_source_into_replica_folder(
            os_independent_path_source_folder,
            os_independent_path_replica_folder,
            os_independent_path_log_file,
        )
        await asyncio.sleep(synchronization_interval)


asyncio.run(synchronize_periodically(synchronization_interval))
