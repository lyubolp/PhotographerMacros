"""
Contains the classes related to the Query abstraction.
Unlike presets, which return an image, queries return a value and do not require a target image.
"""
from typing import Callable


class Query:
    """
    A Query is a function that returns a value.
    """
    def __init__(self, name: str, description: str, executable: Callable) -> None:
        self.__name = name
        self.__description = description
        self.__executable = executable

    def __eq__(self, other):
        return self.name == other.name and self.executable == other.executable

    def __str__(self):
        return self.__name + ": " + self.__description

    @property
    def name(self) -> str:
        """
        Returns the name of the query

        :return: Name of the query
        """
        return self.__name

    @property
    def description(self) -> str:
        """
        Returns the description of the query

        :return: Description of the query
        """
        return self.__description

    @property
    def executable(self) -> Callable:
        """
        Returns the function to be executed

        :return: The function to be executed
        """
        return self.__executable
