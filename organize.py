import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEO": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png'],
}


def pick_directory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC"


def organize_directory():
    for item in os.scandir():
        if item.is_dir():
            continue
        file_path = Path(item)
        file_type = file_path.suffix.lower()
        directory = pick_directory(file_type)
        directory_path = Path(directory)
        if not directory_path.is_dir():
            directory_path.mkdir()
        file_path.rename(directory_path.joinpath(file_path))


organize_directory()
