from enum import Enum
from typing import List


class ActionTypes(Enum):
    enhanceAction = 0,
    filter = 1,
    custom = 2


class Step:
    def __init__(self, name, value, executable, action_type: ActionTypes):
        self.__name = name
        self.__value = value
        self.__executable = executable
        self.__action_type = action_type

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self):
        return self.__value

    @property
    def executable(self):
        return self.__executable

    @property
    def action_type(self) -> ActionTypes:
        return self.__action_type


class Preset:
    def __init__(self, name: str, steps: List[Step]):
        self.__name = name
        self.__steps = steps

    def append(self, action: Step):
        self.__steps.append(action)

    @property
    def steps(self) -> List[Step]:
        return self.__steps

    @property
    def name(self) -> str:
        return self.__name

