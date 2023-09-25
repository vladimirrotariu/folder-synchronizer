# THE IMPLEMENTATION IN WHICH BY CHANGING A FOLDER NAME, THE CONTENT DOES NOT RE-SYNC
"""
    for (
        path_file_source,
        hashed_file_source,
    ) in paths_hashes_files_source.items():
        name_file_source = os.path.basename(path_file_source)

        relative_path_source_file = os.path.relpath(
            path_file_source, path_source_folder
        )

        to_be_path_file_replica = os.path.join(
            path_replica_folder, relative_path_source_file
        )

        if hashed_file_source not in paths_hashes_files_replica.values():
            shutil.copy2(
                path_file_source,
                os.path.dirname(to_be_path_file_replica),
            )
            print(
                "Copied for the first time",
                path_file_source,
                os.path.dirname(to_be_path_file_replica),
            )
        else:
            excluded_count = 0
            files_replica_subdirectory_count = 0
            # diffnamed_copies_source_count = 0
            diffnamed_copies_replica_count = 0

            for (
                path_file_replica,
                hashed_file_replica,
            ) in paths_hashes_files_replica.items():
                relative_path_replica_file = os.path.relpath(
                    path_file_replica, path_replica_folder
                )
                name_file_replica = os.path.basename(path_file_replica)
                if relative_path_replica_file == relative_path_source_file:
                    files_replica_subdirectory_count += 1

                    if hashed_file_replica != hashed_file_source:
                        excluded_count += 1

                    if (
                        hashed_file_replica == hashed_file_source
                        and name_file_replica != name_file_source
                    ):
                        diffnamed_copies_replica_count += 1

            if (
                excluded_count == files_replica_subdirectory_count
                and excluded_count != 0
            ):
                shutil.copy2(
                    path_file_source,
                    os.path.dirname(to_be_path_file_replica),
                )
                print("Copy files with already existing content")

         

            for (
                path_file,
                hashed_file,
            ) in paths_hashes_files_source.items():
                if (
                    os.path.dirname(path_file) == os.path.dirname(path_file_source)
                    and os.path.basename(path_file) != name_file_source
                    and hashed_file == hashed_file_source
                ):
                    diffnamed_copies_source_count += 1

            for _ in range(
                diffnamed_copies_source_count - diffnamed_copies_replica_count
            ):
                for path_file in paths_hashes_files_replica.keys():
                    if os.path.basename(
                        path_file
                    ) != name_file_source and os.path.dirname(
                        path_file
                    ) == os.path.dirname(
                        path_file_source
                    ):
                        renaming_path = os.path.join(
                            os.path.dirname(path_file), name_file_source
                        )
                        os.rename(path_file, renaming_path)
                        print("RENAMED", path_file, renaming_path)

           

            for (
                path_file,
                hashed_file,
            ) in paths_hashes_files_replica.items():
                relative_path_file = os.path.relpath(path_file, path_replica_folder)
                if relative_path_file == relative_path_source_file:
                    if (
                        os.path.basename(path_file) != name_file_source
                        and hashed_file == hashed_file_source
                    ):
                        diffnamed_copies_replica_count += 1

            for _ in range(
                diffnamed_copies_source_count - diffnamed_copies_replica_count
            ):
                
                if all(
                    os.path.basename(path_file_replica) != name_file_source
                    for path_file_replica, hashed_file_replica in paths_hashes_files_replica_folder.items()
                    if os.path.dirname(path_file_replica) == subdirectory_path_replica
                    and hashed_file_source == hashed_file_replica
                ) and any(
                    os.path.basename(path_file_replica) != name_file_source
                    for path_file_replica, hashed_file_replica in paths_hashes_files_replica_folder.items()
                    if os.path.dirname(path_file_replica) == subdirectory_path_replica
                    and hashed_file_source == hashed_file_replica
                ):
                    renaming_path = os.path.join(
                        subdirectory_path_replica, name_file_source
                    )
                    os.rename(
                        path_file_replica,
                        renaming_path,
                    )
                    print(
                        "Named locally",
                        path_file_replica,
                        renaming_path,
                    )
                    break
        """

"""
        if hashed_file_source not in paths_hashes_files_replica_folder.values():
            shutil.copy2(
                path_file_source, to_be_path_file_replica, follow_symlinks=False
            )
            print("Copied from source", path_file_source)
        elif to_be_path_file_replica not in paths_hashes_files_replica_folder.keys():
            for (
                path_file_replica,
                hashed_file_replica,
            ) in paths_hashes_files_replica_folder.items():
                name_file_source = os.path.basename(path_file_source)
                name_file_replica = os.path.basename(path_file_replica)
                subdirectory_path_replica = os.path.dirname(path_file_replica)

                if all(
                    name_file_replica != name_file_source
                    for path_file_replica in paths_hashes_files_replica_folder.keys()
                    if os.path.dirname(path_file_replica) == subdirectory_path_replica
                ):
                    shutil.copy2(
                        path_file_replica,
                        to_be_path_file_replica,
                    )
                    print(
                        "Copied locally",
                        path_file_replica,
                        to_be_path_file_replica,
                    )
                    break
        """
