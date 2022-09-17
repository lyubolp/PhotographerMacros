"""
Contains the parse_args function, used for CLI parsing
"""

import argparse

from mode import Mode


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

    parser.add_argument("-v", "--verbosity", action="store_true", default=False,
                      help="Show more info on stdout")
    parser.add_argument("-q", "--quiet", action="store_true", default=False,
                      help="Doesn't show anything on the stdout")

    subparser = parser.add_subparsers(dest='mode')

    edit = subparser.add_parser('edit')

    edit.add_argument("source", type=str, help="Source image", nargs="?", default="")
    edit.add_argument("target", type=str, help="Destination path", nargs="?", default="")
    edit.add_argument("preset", type=str, help="Which preset to be applied", nargs="?",
                        default="")

    edit.add_argument("-l", "--list", action="store_true", default=False,
                        help="Show a list of presets")

    organize = subparser.add_parser('organize')
    organize.add_argument("work_dir", type=str, help="Working directory", nargs="?", default="")

    if args is None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    args = args.__dict__

    args['mode'] = Mode.from_str(args['mode'])

    return args
