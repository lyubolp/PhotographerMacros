"""
Module containing the CLITests class
"""

import unittest
from src.cli import parse_args


class CLITests(unittest.TestCase):
    """
    Contains unittests for the CLI module
    """
    def test_01_list(self):
        arguments = ['-l']
        result = parse_args(arguments)
        self.assertTrue(result['list'])

    def test_02_verbosity(self):
        arguments = ['-v']
        result = parse_args(arguments)
        self.assertTrue(result['verbosity'])

    def test_03_quiet(self):
        arguments = ['-q']
        result = parse_args(arguments)
        self.assertTrue(result['quiet'])

    def test_04_source(self):
        arguments = ['foo']
        result = parse_args(arguments)
        self.assertEqual(arguments[0], result['source'])

    def test_05_target(self):
        arguments = ['foo', 'bar']
        result = parse_args(arguments)
        self.assertEqual(arguments[1], result['target'])

    def test_06_preset(self):
        arguments = ['foo', 'bar', 'baz']
        result = parse_args(arguments)
        self.assertEqual(arguments[2], result['preset'])


if __name__ == '__main__':
    unittest.main()
