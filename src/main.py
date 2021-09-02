import os
from PIL import Image
from functools import reduce

from cli import parse_args
from preset import Step, ActionTypes
from presets import load_presets
from output import OutputHandler


def execute_step(img: Image, step: Step) -> Image:
    output.print("Applying {} with value {}".format(step.name, step.value))

    if step.action_type == ActionTypes.enhanceAction:
        obj = step.executable(img)
        img = obj.enhance(step.value)
    elif step.action_type == ActionTypes.filter:
        img = img.filter(step.executable)
    elif step.action_type == ActionTypes.custom:
        img = step.executable(img, step.executable)

    return img


if __name__ == "__main__":

    args = parse_args()
    presets = load_presets()

    output_level = 1
    if args["verbosity"]:
        output_level = 2
    elif args["quiet"]:
        output_level = 0

    output = OutputHandler(output_level)
    output.print("Args: {}".format(args), 2)
    output.print("Presets: {}".format(presets), 2)

    if args["list"]:
        output.print("Available presets:")
        for preset in presets:
            output.print(" - " + preset.name)
        exit(0)

    source_image = args["source"]
    if not os.path.isfile(source_image):
        output.print("Error 1: Invalid source path")
        exit(1)

    target_image = args["target"]

    preset_name = args["preset"]
    if preset_name not in [p.name for p in presets]:
        output.print("Invalid preset name")
        exit(1)

    # There should be exactly one preset with the given name
    preset = [p for p in presets if p.name == preset_name][0]

    output.print("Applying preset {} to {}. Result will be written at {}".format(preset_name, source_image, target_image))

    with Image.open(source_image) as im:
        # Really cool way to apply the steps to the image one by one
        # https://docs.python.org/3/library/functools.html?highlight=reduce#functools.reduce
        im = reduce(execute_step, preset.steps, im)

        im.save(target_image)

    output.print("Done", 1)
