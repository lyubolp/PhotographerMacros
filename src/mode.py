from enum import Enum


class Mode(Enum):
    EDIT = 0
    ORGANIZE = 1

    @staticmethod
    def from_str(mode: str):
        str_to_enum = {
            'edit': 0,
            'organize': 1
        }

        return Mode(str_to_enum[mode])
