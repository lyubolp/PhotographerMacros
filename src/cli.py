"""
Contains the parse_args function, used for CLI parsing
"""

import argparse


def parse_args(args: list = None) -> dict:
    """
    Parses the command line arguments
    :param args: Optional, used for testing
    :return: Dictionary, containing the parsed arguments and their values
    """
    parser = argparse.ArgumentParser(
        prog="photographerMacros",
        description="A CLI tool which applies filters to photos",
        add_help=True
    )

    parser.add_argument("source", type=str, help="Source image", nargs="?", default="")
    parser.add_argument("target", type=str, help="Destination path", nargs="?", default="")
    parser.add_argument("preset", type=str, help="Which preset to be applied", nargs="?",
                        default="")

    parser.add_argument("-l", "--list", action="store_true", default=False,
                        help="Show a list of presets")
    parser.add_argument("-v", "--verbosity", action="store_true", default=False,
                        help="Show more info on stdout")
    parser.add_argument("-q", "--query", type=str, help="Execute a query")
    parser.add_argument("--quiet", action="store_true", default=False,
                        help="Doesn't show anything on the stdout")

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    return args.__dict__
