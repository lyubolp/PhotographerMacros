"""
Module that changes the color balance of an image
"""
from typing import List
from PIL import Image


def change_color_balance(image: Image.Image, factors: List[float]) -> Image.Image:
    """
    Function that changes the color balance by multiplying the image matrix by another matrix
    containing the factors for each channel
    :param image: The image to be changed
    :param factors: List, containing the red, green and blue factor to be applied
    :return: The resulting image
    """
    matrix = (factors[0], 0.0,        0.0,        0.0,
              0.0,        factors[1], 0.0,        0.0,
              0.0,        0.0,        factors[2], 0.0)

    return image.convert("RGB", matrix)
