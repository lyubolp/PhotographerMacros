import os
from PIL import Image, ImageEnhance

from src.cli import parse_args
from src.presets import read_presets


def generate_object_from_action(action_name):
    objects = {
        "color": ImageEnhance.Color,
        "contrast": ImageEnhance.Contrast,
        "brightness": ImageEnhance.Brightness
    }

    return objects[action_name]


if __name__ == "__main__":

    args = parse_args()

    presets = read_presets()

    if args["verbosity"]:
        print(args)
        print(presets)

    source_image = args["source"]

    if not os.path.isfile(source_image):
        print("Invalid source path")
        exit(1)

    target_image = args["target"]

    preset_name = args["preset"]

    if preset_name not in [p["name"] for p in presets]:
        print("Invalid preset name")
        exit(1)

    # There should be exactly one preset with the given name
    preset = [p for p in presets if p["name"] == preset_name][0]

    steps = [(action, preset[action]) for action in list(preset.keys())[1:]]

    print("Applying preset {} to {}. Result will be written at {}".format(preset_name, source_image, target_image))

    with Image.open(source_image) as im:

        for step in steps:
            print("Applying {} with value {}".format(step[0], step[1]))
            obj = generate_object_from_action(step[0])(im)
            im = obj.enhance(step[1])

        im.save(target_image)