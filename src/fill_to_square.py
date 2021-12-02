from typing import List

from PIL import Image
import numpy as np


def __expand_left(image: np.array, color: List[int], size: int, by: int) -> np.array:
    column = np.tile(color, size).reshape((size, 3))
    return np.append(np.tile(column, by).reshape((size, by, 3)), image, 1)


def __expand_right(image: np.array, color: List[int], size: int, by: int) -> np.array:
    column = np.tile(color, size).reshape((size, 3))
    return np.append(image, np.tile(column, by).reshape((size, by, 3)), 1)


def __expand_up(image: np.array, color: List[int], size: int, by: int) -> np.array:
    row = np.tile(color, size).reshape((size, 3))
    return np.append(np.tile(row, by).reshape((by, size, 3)), image, 0)


def __expand_down(image: np.array, color: List[int], size: int, by: int) -> np.array:
    row = np.tile(color, size).reshape((size, 3))
    return np.append(image, np.tile(row, by).reshape((by, size, 3)), 0)


def fill_to_square(image: Image, color_to_fill: str) -> Image:
    image_as_np = np.asarray(image)

    height = np.size(image_as_np, axis=0)
    width = np.size(image_as_np, axis=1)

    # TODO - This could be refactored
    color_without_pound = color_to_fill[1:]

    red = int(color_without_pound[:2], base=16)
    green = int(color_without_pound[2:4], base=16)
    blue = int(color_without_pound[4:6], base=16)

    color = np.array([red, green, blue], dtype='uint8')

    if height > width:
        expand_with = (height - width) // 2
        image_as_np = __expand_left(image_as_np, color, height, expand_with)
        image_as_np = __expand_right(image_as_np, color, height, expand_with)
    else:
        expand_with = (width - height) // 2
        image_as_np = __expand_up(image_as_np, color, width, expand_with)
        image_as_np = __expand_down(image_as_np, color, width, expand_with)

    return Image.fromarray(image_as_np)
