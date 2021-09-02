import json
from typing import List
from PIL import Image, ImageEnhance, ImageFilter

from change_color_balance import change_color_balance
from color_temperature import change_temperature
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
    "emboss": (ImageFilter.EMBOSS, ActionTypes.filter)
}


def load_presets(path="presets.json") -> List[Preset]:
    presets_dict = {}
    with open(path) as f:
        presets_dict = json.loads(f.read())["presets"]

    # TODO - Add error handling

    result = []
    for preset in presets_dict:
        steps = [Step(action, preset[action], objects[action][0], objects[action][1]) for action in preset.keys() if
                 action != "name"]
        preset = Preset(preset['name'], steps)
        result.append(preset)

    return result
