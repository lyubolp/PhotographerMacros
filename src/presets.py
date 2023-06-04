"""
Contains logic for parsing the presets saved in the JSON
"""
import json
from typing import List
from PIL import ImageEnhance, ImageFilter

from src.change_color_balance import change_color_balance
from src.color_temperature import change_temperature
from src.preset import Preset, Step, ActionTypes

objects = {
    "color": (ImageEnhance.Color, ActionTypes.ENHANCE_ACTION),
    "contrast": (ImageEnhance.Contrast, ActionTypes.ENHANCE_ACTION),
    "brightness": (ImageEnhance.Brightness, ActionTypes.ENHANCE_ACTION),
    "sharpness": (ImageEnhance.Sharpness, ActionTypes.ENHANCE_ACTION),
    "blur": (ImageFilter.BLUR, ActionTypes.FILTER),
    "contour": (ImageFilter.CONTOUR, ActionTypes.FILTER),
    "detail": (ImageFilter.DETAIL, ActionTypes.FILTER),
    "edge_enhance": (ImageFilter.EDGE_ENHANCE, ActionTypes.FILTER),
    "sharpen": (ImageFilter.SHARPEN, ActionTypes.FILTER),
    "smooth": (ImageFilter.SMOOTH, ActionTypes.FILTER),
    "temperature": (change_temperature, ActionTypes.CUSTOM),
    "color_balance": (change_color_balance, ActionTypes.CUSTOM),
    "emboss": (ImageFilter.EMBOSS, ActionTypes.FILTER)
}


def load_presets(path="presets.json", objects_dict=None) -> List[Preset]:
    """
    Parses the presets from a JSON file

    :param path: Path to the JSON file containing the file presets
    :param objects_dict: A mapping of the filters
        - contains tuples of the function to be called and the type
    :return: List containing `Preset` instances
    """
    if objects_dict is None:
        objects_dict = objects

    with open(path, encoding="utf-8") as file_handler:
        presets_dict = json.loads(file_handler.read())["presets"]

    result = []
    for preset in presets_dict:

        name = preset['name']
        del preset['name']

        description = ""

        if 'description' in preset:
            description = preset['description']
            del preset['description']

        steps = [Step(action, preset[action], objects_dict[action][0], objects_dict[action][1])
                 for action in preset.keys()]
        preset = Preset(name, description, steps)
        result.append(preset)

    return result
