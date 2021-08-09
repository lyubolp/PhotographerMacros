import os

from PIL import Image, ImageEnhance
from cli import parse_args

if __name__ == "__main__":

    args = parse_args()
    print(args)

    source_image = args["source"]

    if not os.path.isfile(source_image):
        print("Invalid source path")
        exit(1)

    target_image = args["target"]

    with Image.open(source_image) as im:
        color = ImageEnhance.Color(im)
        after_color = color.enhance(1.5)

        after_color.save("../after_color.jpg")

        contrast = ImageEnhance.Contrast(after_color)
        after_contrast = contrast.enhance(1.5)

        after_contrast.save("../after_contrast.jpg")
