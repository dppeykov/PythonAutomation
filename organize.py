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
    # scandir will return an object with all the contents of the current directory, where the script is executing
    for item in os.scandir(): 
        if item.is_dir(): # if it is a directory - we are skipping it
            continue
        file_path = Path(item) # gets the name of the files in the directory - name.suffix
        file_type = file_path.suffix.lower()  # returns .txt, .pdf ...
        directory = pick_directory(file_type) # uses the pick directory function to choose the right dir for the file
        directory_path = Path(directory)
        if not directory_path.is_dir(): # if the directory doen't exist - it will create it with mkdir()
            directory_path.mkdir()
        file_path.rename(directory_path.joinpath(file_path)) # will move the file to the appropriate folder


organize_directory()
