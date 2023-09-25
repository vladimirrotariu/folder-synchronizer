import hashlib
import os


def hash_file(file_name: str) -> str:
    sha256_handler = hashlib.sha256()

    with open(file_name, "rb") as file:
        while True:
            half_a_megabyte_batch: bytes = file.read(2**19)

            if not half_a_megabyte_batch:
                break

            sha256_handler.update(half_a_megabyte_batch)

    hashed_binary_file = sha256_handler.hexdigest()

    return hashed_binary_file


def hash_folder_files(path_folder: str):
    paths_hashes_files = {}
    directory_paths = []

    for directory_path, directory_names, file_names in os.walk(path_folder):
        directory_paths.append(directory_path)

        for directory_name in directory_names:
            inner_directory_path = os.path.join(directory_path, directory_name)
            directory_paths.append(inner_directory_path)

        for file_name in file_names:
            os.chdir(directory_path)

            directory_name = os.path.dirname(path_folder)

            trunked_directory_path = directory_path.replace(
                f"{os.path.sep}{directory_name}", ""
            )

            file_path = os.path.join(trunked_directory_path, file_name)

            paths_hashes_files[f"{file_path}"] = [hash_file(file_name)]

    return [directory_paths, paths_hashes_files]
