import asyncio

from project_source_to_replica import (
    project_source_into_replica,
)
from utils import (
    read_path,
    validate_folder_path,
    read_time_interval,
)

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

synchronization_interval: float = read_time_interval()


async def synchronize_periodically(synchronization_interval: float) -> None:
    while True:
        await project_source_into_replica(
            os_independent_path_source_folder,
            os_independent_path_replica_folder,
            os_independent_path_log_file,
        )
        await asyncio.sleep(synchronization_interval)


asyncio.run(synchronize_periodically(synchronization_interval))
