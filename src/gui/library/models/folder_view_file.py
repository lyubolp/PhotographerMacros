"""
Contains the classes related to the folder view file handling
"""
from typing import List


class FolderViewFile:
    """
    Represents a file in the folder view
    """
    def __init__(self, filename: str, path: str):
        self.__filename = filename
        self.__path = path
        self.__is_marked = False
    
    @property
    def filename(self) -> str:
        """
        Returns the filename of the image
        """
        return self.__filename

    @property
    def path(self) -> str:
        """
        Returns the path of the image
        """
        return self.__path

    @property
    def is_marked(self) -> bool:
        """
        Returns whether the image is marked
        """
        return self.__is_marked

    def mark(self):
        """
        Marks the image
        """
        self.__is_marked = True

    def unmark(self):
        """
        Unmarks the image
        """
        self.__is_marked = False
    
    def toogle_mark(self):
        """
        Toogle the mark of the image
        """
        self.__is_marked = not self.__is_marked


class FolderViewFiles:
    def __init__(self, root_dir: str):
        self.__files: List[FolderViewFile] = []
        self.__current_index = 0
        self.__root_dir = root_dir

    def add_file(self, filename: str, path: str):
        """
        Adds a file to the list
        """
        self.__files.append(FolderViewFile(filename, path))

    def get_file_by_index(self, index: int) -> FolderViewFile:
        """
        Returns the file by index
        """
        return self.__files[index]

    def get_file_by_filename(self, filename: str) -> FolderViewFile:
        """
        Returns the file by filename
        """
        for file in self.__files:
            if file.filename == filename:
                return file

        raise ValueError(f"File {filename} not found")

    def get_filenames(self) -> List[str]:
        """
        Returns the list of filenames
        """
        return [file.filename for file in self.__files]
