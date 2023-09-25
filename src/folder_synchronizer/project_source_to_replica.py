import os
import shutil
from hashing_content import hash_folder_files

from utils import (
    create_directories,
    rename_files,
)


async def project_source_into_replica(
    path_source_folder: str, path_replica_folder: str, path_log_file: str
):
    directory_paths_source, paths_hashes_files_source = hash_folder_files(
        path_source_folder
    )

    create_directories(path_source_folder, path_replica_folder, directory_paths_source)

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
                reporting_pattern = (
                    f"CPY FILE FROM DIR {os.path.dirname(path_file_source)}"
                    + f"TO {os.path.dirname(to_be_path_file_replica)}"
                )
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

            rename_files(subpaths_source, subpaths_replica)
