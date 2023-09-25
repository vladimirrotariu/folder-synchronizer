from utils import create_directories
import os

# PROVIDING EXAMPLES OF PATHS THAT I USED


def test_create_directories():
    """
    GIVEN a function create_directories that creates a directory skeleton
    """

    path_source_test = "/Users/vladimirioanrotariu/Desktop/gg/test_source"
    path_replica_test = "/Users/vladimirioanrotariu/Desktop/gg/test_replica"
    directory_paths_source = [
        "/Users/vladimirioanrotariu/Desktop/gg/test_source/folder_1a/folder_2a",
        "/Users/vladimirioanrotariu/Desktop/gg/test_source/folder_1a/folder_2b",
        "/Users/vladimirioanrotariu/Desktop/gg/test_source/folder_1b/folder_2a",
    ]

    """
    WHEN it is called with parameters a source and replica directories, as well as the directory skeleton of the source
    """

    create_directories(path_source_test, path_replica_test, directory_paths_source)

    """
    THEN it should recreate the directory skeleton of the source in the replica
    """

    for directory_path in directory_paths_source:
        assert os.path.isdir(directory_path)
