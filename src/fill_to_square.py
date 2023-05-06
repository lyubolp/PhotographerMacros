"""
Module containing the function to fill an image to a square.
"""
from typing import List

from PIL import Image
import numpy as np


def __expand_left(image: np.ndarray, color: List[int], size: int, amount: int) -> np.ndarray:
    column = np.tile(color, size).reshape((size, 3))
    return np.append(np.tile(column, amount).reshape((size, amount, 3)), image, 1)


def __expand_right(image: np.ndarray, color: List[int], size: int, amount: int) -> np.ndarray:
    column = np.tile(color, size).reshape((size, 3))
    return np.append(image, np.tile(column, amount).reshape((size, amount, 3)), 1)


def __expand_up(image: np.ndarray, color: List[int], size: int, amount: int) -> np.ndarray:
    row = np.tile(color, size).reshape((size, 3))
    return np.append(np.tile(row, amount).reshape((amount, size, 3)), image, 0)


def __expand_down(image: np.ndarray, color: List[int], size: int, amount: int) -> np.ndarray:
    row = np.tile(color, size).reshape((size, 3))
    return np.append(image, np.tile(row, amount).reshape((amount, size, 3)), 0)


def fill_to_square(image: Image.Image, color_to_fill: str) -> Image.Image:
    """
    Expands an image to a square by filling the missing space with a color.

    :param image: The image to expand.
    :param color_to_fill: The color to fill the missing space with.
    :return: The expanded image.
    """
    image_as_np = np.asarray(image)

    height = np.size(image_as_np, axis=0)
    width = np.size(image_as_np, axis=1)

    # TODO - This could be refactored
    color_without_pound = color_to_fill[1:]

    red = int(color_without_pound[:2], base=16)
    green = int(color_without_pound[2:4], base=16)
    blue = int(color_without_pound[4:6], base=16)

    color = [red, green, blue]

    if height > width:
        expand_with = (height - width) // 2
        image_as_np = __expand_left(image_as_np, color, height, expand_with)
        image_as_np = __expand_right(image_as_np, color, height, expand_with)
    else:
        expand_with = (width - height) // 2
        image_as_np = __expand_up(image_as_np, color, width, expand_with)
        image_as_np = __expand_down(image_as_np, color, width, expand_with)

    return Image.fromarray(image_as_np)
