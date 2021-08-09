class OutputHandler:
    def __init__(self, level):
        """
        Initializes the output handler
        Levels:
        0 - quiet
        1 - normal
        2 - verbose

        :param level:
        """
        self._level = level

    def print(self, message: str, target_level: int = 1):
        if target_level <= self._level:
            print(message)