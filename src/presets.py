"""
Contains logic for parsing the presets saved in the JSON
"""
import json
from typing import List
from PIL import ImageEnhance, ImageFilter

from change_color_balance import change_color_balance
from color_temperature import change_temperature
from portrait_mode import portrait_mode
from preset import Preset, Step, ActionTypes

objects = {
    "color": (ImageEnhance.Color, ActionTypes.enhanceAction),
    "contrast": (ImageEnhance.Contrast, ActionTypes.enhanceAction),
    "brightness": (ImageEnhance.Brightness, ActionTypes.enhanceAction),
    "sharpness": (ImageEnhance.Sharpness, ActionTypes.enhanceAction),
    "blur": (ImageFilter.BLUR, ActionTypes.filter),
    "contour": (ImageFilter.CONTOUR, ActionTypes.filter),
    "detail": (ImageFilter.DETAIL, ActionTypes.filter),
    "edge_enhance": (ImageFilter.EDGE_ENHANCE, ActionTypes.filter),
    "sharpen": (ImageFilter.SHARPEN, ActionTypes.filter),
    "smooth": (ImageFilter.SMOOTH, ActionTypes.filter),
    "temperature": (change_temperature, ActionTypes.custom),
    "color_balance": (change_color_balance, ActionTypes.custom),
    "emboss": (ImageFilter.EMBOSS, ActionTypes.filter),
    "portrait_mode": (portrait_mode, ActionTypes.custom)
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

    with open(path) as file_handler:
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
