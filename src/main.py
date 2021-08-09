import os
from enum import Enum
from PIL import Image, ImageEnhance, ImageFilter

from cli import parse_args
from presets import read_presets
from color_temperature import change_temperature
from output import OutputHandler


class ActionTypes(Enum):
    enhanceAction = 0,
    filter = 1,
    custom = 2


def generate_object_from_action(action_name):
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
        "temperature": (change_temperature, ActionTypes.custom)
    }

    return objects[action_name]


if __name__ == "__main__":

    args = parse_args()
    presets = read_presets()

    output_level = 1
    if args["verbosity"]:
        output_level = 2
    elif args["quiet"]:
        output_level = 0

    output = OutputHandler(output_level)

    output.print("Args: {}".format(args), 2)
    output.print("Presets: {}".format(presets), 2)

    source_image = args["source"]

    if not os.path.isfile(source_image):
        output.print("Invalid source path", 1)
        exit(1)

    target_image = args["target"]

    preset_name = args["preset"]

    if preset_name not in [p["name"] for p in presets]:
        output.print("Invalid preset name", 1)
        exit(1)

    # There should be exactly one preset with the given name
    preset = [p for p in presets if p["name"] == preset_name][0]

    steps = [(action, preset[action]) for action in list(preset.keys())[1:]]

    output.print("Applying preset {} to {}. Result will be written at {}".format(preset_name, source_image, target_image), 1)

    with Image.open(source_image) as im:

        for step in steps:
            output.print("Applying {} with value {}".format(step[0], step[1]), 1)

            module, action_type = generate_object_from_action(step[0])

            if action_type == ActionTypes.enhanceAction:
                obj = module(im)
                im = obj.enhance(step[1])
            elif action_type == ActionTypes.filter:
                im = im.filter(module)
            elif action_type == ActionTypes.custom:
                im = module(im, step[1])

        im.save(target_image)

    output.print("Done", 1)
