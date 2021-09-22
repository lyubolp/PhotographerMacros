"""
Contains the OutputHandler class, used for output in the application
"""


class OutputHandler:
    """
    Class that takes care of the output (allowing for verbose/normal/quiet options
    """
    def __init__(self, level):
        """
        Initializes the output handler
        Levels:
        0 - quiet
        1 - normal
        2 - verbose

        :param level: Sets the level
        """
        self._level = level

    def print(self, message: str, target_level: int = 1):
        """
        Method used for printing messages to the proper location

        :param message:
        :param target_level:
        :return:
        """
        if target_level <= self._level:
            print(message)
