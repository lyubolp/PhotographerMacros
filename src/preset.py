"""
Contains classes related to the Preset abstraction - ActionTypes, Step and Preset
"""
from enum import Enum
from typing import List


class ActionTypes(Enum):
    """
    Enums that keeps the type of an action - "enhance" & "filter" are from the PIL library,
    while the "custom" one represents a custom action (not part of the PIL lib)
    """
    enhanceAction = 0
    filter = 1
    custom = 2


class Step:
    """
    Represents a single filter to be applied to an image.
    Keeps the name, value, function to be applied and the ActionType of a step
    """
    def __init__(self, name, value, executable, action_type: ActionTypes):
        self.__name = name
        self.__value = value
        self.__executable = executable
        self.__action_type = action_type

    def __eq__(self, other) -> bool:
        return all([self.name == other.name,
                    self.value == other.value,
                    self.action_type == other.action_type])

    @property
    def name(self) -> str:
        """
        Returns the name of the step

        :return: String, containing the name
        """
        return self.__name

    @property
    def value(self):
        """
        Returns the value with which the step will be applied. Pass to the executable.

        :return: The value (type not specified)
        """
        return self.__value

    @property
    def executable(self):
        """
        Returns the function to be applied to an image

        :return: The function pointer
        """
        return self.__executable

    @property
    def action_type(self) -> ActionTypes:
        """
        Returns the type of the Step

        :return: ActionType object, representing the type of step
        """
        return self.__action_type


class Preset:
    """
    A Preset objects represents a collection of steps to be applied to an image
    """
    def __init__(self, name: str, description: str, steps: List[Step]):
        self.__name = name
        self.__description = description
        self.__steps = steps

    def __eq__(self, other):
        return self.name == other.name and self.steps == other.steps

    def __str__(self):
        return self.__name + ": " + self.__description

    def append(self, action: Step):
        """
        Adds a Step to the Preset

        :param action: The step to be added
        """
        self.__steps.append(action)

    @property
    def steps(self) -> List[Step]:
        """
        Returns a list of steps to be applied when a given preset is selected

        :return: List, containing `Step` objects
        """
        return self.__steps

    @property
    def name(self) -> str:
        """
        Returns the name of the preset

        :return: String, containing the name of the preset
        """
        return self.__name

    @property
    def description(self) -> str:
        return self.__description
