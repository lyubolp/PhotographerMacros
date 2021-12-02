import unittest
import numpy as np
from PIL import Image

from src.fill_to_square import fill_to_square


class FillToSquareTests(unittest.TestCase):
    def test_01_horizontal_image(self):
        initial_image = np.ones((10, 20, 3), dtype='uint8')

        left_expand = np.append(np.zeros((5, 20, 3), dtype='uint8'), initial_image).reshape(
            (15, 20, 3))
        expected_image = np.append(left_expand, np.zeros((5, 20, 3), dtype='uint8')).reshape(
            (20, 20, 3))

        result_image = fill_to_square(Image.fromarray(initial_image), "#000000")
        self.assertTrue((expected_image == np.asarray(result_image)).all())

    def test_02_vertical_image(self):
        initial_image = np.ones((20, 10, 3), dtype='uint8')

        top_expand = np.append(np.zeros((20, 5, 3), dtype='uint8'), initial_image, 1).reshape(
            (20, 15, 3))
        expected_image = np.append(top_expand, np.zeros((20, 5, 3), dtype='uint8'), 1).reshape(
            (20, 20, 3))

        result_image = fill_to_square(Image.fromarray(initial_image), "#000000")

        self.assertTrue((expected_image == np.asarray(result_image)).all())


if __name__ == '__main__':
    unittest.main()
