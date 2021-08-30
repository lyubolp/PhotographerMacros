from typing import List
from PIL import Image


def change_color_balance(image: Image, factors: List[float]) -> Image:
    matrix = (factors[0], 0.0,        0.0,        0.0,
              0.0,        factors[1], 0.0,        0.0,
              0.0,        0.0,        factors[2], 0.0)

    return image.convert("RGB", matrix)
