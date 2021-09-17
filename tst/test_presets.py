import json
import os
import unittest
from json import JSONDecodeError

from preset import Preset, Step, ActionTypes
from presets import load_presets


def default_action_1(value: float):
    return value


def default_action_2(value: bool):
    return value


def default_action_3(value: int):
    return value


def default_action_4(value: bool):
    return value


class TestPresets(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp_file_path = "/tmp/temp_json.json"

    def tearDown(self) -> None:
        if os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

    def test_01_valid_json(self):
        mocked_json = {
            "presets": [
                {
                    "name": "preset1",
                    "step1": 1.5,
                    "step2": True
                },
                {
                    "name": "preset2",
                    "step3": 3000,
                    "step4": False
                }
            ]
        }

        json_to_write = json.dumps(mocked_json, indent=4)

        with open(self.temp_file_path, "w+") as f:
            f.write(json_to_write)

        mocked_objects = {
            "step1": (default_action_1, ActionTypes.filter),
            "step2": (default_action_2, ActionTypes.enhanceAction),
            "step3": (default_action_3, ActionTypes.custom),
            "step4": (default_action_4, ActionTypes.filter),
        }

        loaded_presets = load_presets(self.temp_file_path, mocked_objects)
        self.assertEqual(2, len(loaded_presets))

        expected_presets = [Preset("preset1",
                                   [Step("step1", 1.5, default_action_1, ActionTypes.filter),
                                    Step("step2", True, default_action_2, ActionTypes.enhanceAction)]),
                            Preset("preset2",
                                   [Step("step3", 3000, default_action_3, ActionTypes.custom),
                                    Step("step4", False, default_action_4, ActionTypes.filter)])
                            ]

        for index, preset in enumerate(loaded_presets):
            self.assertEqual(expected_presets[index], preset)

    def test_02_invalid_json(self):
        with open(self.temp_file_path, "w+") as f:
            f.write("invalid json")
        self.assertRaises(JSONDecodeError, load_presets, self.temp_file_path)

    def test_03_invalid_file(self):
        self.assertRaises(OSError, load_presets, self.temp_file_path)

    def test_04_empty_file(self):
        open(self.temp_file_path, "w+")
        self.assertRaises(JSONDecodeError, load_presets, self.temp_file_path)


if __name__ == '__main__':
    unittest.main()
