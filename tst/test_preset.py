import unittest

from src.preset import ActionTypes, Step, Preset


class TestStep(unittest.TestCase):
    def test_01_constructor_and_properties(self):
        temp_name = "name"
        temp_value = "value"
        temp_executable = lambda x: x
        temp_action_type = ActionTypes.filter

        temp_instance = Step(temp_name, temp_value, temp_executable, temp_action_type)

        self.assertEqual(temp_name, temp_instance.name)
        self.assertEqual(temp_value, temp_instance.value)
        self.assertEqual(temp_executable, temp_instance.executable)
        self.assertEqual(temp_action_type, temp_instance.action_type)


class TestPreset(unittest.TestCase):
    def test_01_constructor_and_properties(self):
        temp_names = ["name1", "name2", "name3"]
        temp_values = ["value1", "value2", "value3"]
        temp_executables = [lambda x: x, lambda y: y + 2, lambda z: z + 3]
        temp_action_types = [ActionTypes.filter, ActionTypes.enhanceAction, ActionTypes.custom]

        steps = [Step(temp_names[i], temp_values[i], temp_executables[i], temp_action_types[i]) for i in range(len(temp_names))]

        instance_name = "foo"
        instance_description = "description"
        temp_instance = Preset(instance_name, instance_description, steps)

        self.assertEqual(instance_name, temp_instance.name)
        self.assertEqual(instance_description, temp_instance.description)

        for i, step in enumerate(temp_instance.steps):
            self.assertEqual(steps[i], step)


if __name__ == '__main__':
    unittest.main()
