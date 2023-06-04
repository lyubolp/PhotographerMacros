"""
Module that contains the function to get the dominant color of an image
"""
from typing import Tuple
from PIL import Image


def calculate_dominant_color(image: Image.Image) -> Tuple[int, int, int]:
    """
    Calculate the dominant color of an image
    :param image: Image to calculate the dominant color
    :return: Tuple with the RGB values of the dominant color
    """

    image = image.convert("RGB")
    colors = image.getcolors(maxcolors=1000000)
    colors = sorted(colors, key=lambda item: item[0])

    return colors[-1][1]
