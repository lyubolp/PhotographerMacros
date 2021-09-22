"""
Contains main logic of the app
"""
import os
import sys

from functools import reduce
from PIL import Image

from cli import parse_args
from preset import Step, ActionTypes
from presets import load_presets
from output import OutputHandler


def execute_step(img: Image, step: Step) -> Image:
    """
    Executes a given step on an Image

    :param img: The image on which the filter will be applied
    :param step: The step to be applied
    :return: The resulting image
    """
    output.print("Applying {} with value {}".format(step.name, step.value))

    if step.action_type == ActionTypes.enhanceAction:
        obj = step.executable(img)
        img = obj.enhance(step.value)
    elif step.action_type == ActionTypes.filter:
        img = img.filter(step.executable)
    elif step.action_type == ActionTypes.custom:
        img = step.executable(img, step.value)

    return img


if __name__ == "__main__":

    args = parse_args()
    presets = load_presets()

    OUTPUT_LEVEL = 1
    if args["verbosity"]:
        OUTPUT_LEVEL = 2
    elif args["quiet"]:
        OUTPUT_LEVEL = 0

    output = OutputHandler(OUTPUT_LEVEL)
    output.print("Args: {}".format(args), 2)
    output.print("Presets: {}".format(presets), 2)

    if args["list"]:
        output.print("Available presets:")
        for preset in presets:
            output.print(" - " + preset.name)
        sys.exit(0)

    source_image = args["source"]
    if not os.path.isfile(source_image):
        output.print("Error 1: Invalid source path")
        sys.exit(1)

    target_image = args["target"]

    preset_name = args["preset"]
    if preset_name not in [p.name for p in presets]:
        output.print("Invalid preset name")
        sys.exit(1)

    # There should be exactly one preset with the given name
    preset = [p for p in presets if p.name == preset_name][0]

    output.print("Applying preset {} to {}. Result will be written at {}"
                 .format(preset_name, source_image, target_image))

    with Image.open(source_image) as im:
        # Really cool way to apply the steps to the image one by one
        # https://docs.python.org/3/library/functools.html?highlight=reduce#functools.reduce
        im = reduce(execute_step, preset.steps, im)

        im.save(target_image)

    output.print("Done", 1)
