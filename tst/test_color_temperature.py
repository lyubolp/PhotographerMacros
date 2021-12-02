import unittest
import numpy as np
from PIL import Image

from src.color_temperature import change_temperature


class ColorTemperatureTest(unittest.TestCase):
    def test_01_change_temperature(self):
        row = np.tile([10, 10, 10], 20).reshape((20, 3))
        initial_image = Image.fromarray(np.tile(row, 30).reshape((30, 20, 3)))

        expected_image_row = np.tile([10, 2, 0], 20).reshape((20, 3))
        expected_image = np.tile(expected_image_row, 30).reshape((30, 20, 3))

        result_image = change_temperature(initial_image, 1000)

        self.assertTrue((expected_image == np.asarray(result_image)).all())


if __name__ == '__main__':
    unittest.main()
