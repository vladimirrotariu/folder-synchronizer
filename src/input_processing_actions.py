import re
import os


def read_path(prompt: str) -> str:
    forbidden_characters = re.compile(r"[<>:|?*]")

    path_separator = os.path.sep

    while True:
        path = input(prompt)

        if forbidden_characters.search(path):
            print(
                "Invalid path, you introduced a forbidden character. Try again :)",
                "\n",
            )
        else:
            path_components = path.split(path_separator)

            os_independent_path = os.path.join(path_separator, *path_components)

            return os_independent_path


def read_validate_synchronization_interval() -> float:
    while True:
        raw_synchronization_interval = input(
            "The synchronization interval (in seconds): "
        )

        try:
            synchronization_interval = float(raw_synchronization_interval)
        except ValueError:
            print(
                f"Your input {raw_synchronization_interval} cannot be converted to a number with decimals. Try again :)",
                "\n",
            )
        else:
            if synchronization_interval <= 0:
                print("You introduced a non-positive number. Try again :)")
            else:
                return synchronization_interval


def validate_folder_path(path: str) -> None:
    try:
        if not os.path.exists(path):
            print(
                "The path you provided does not exist. We try to create it for you...",
                "\n",
            )
            os.makedirs(path)
        else:
            if not os.path.isdir(path):
                print(
                    "The path you provided does not have as a base a directory. We try to create it for you...",
                    "\n",
                )
                os.makedirs(path)
    except PermissionError:
        print("You don't have permission to access this path!")
