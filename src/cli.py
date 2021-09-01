import argparse


def parse_args() -> dict:
    parser = argparse.ArgumentParser(
        prog="photographerMacros",
        description="A CLI tool which applies filters to photos",
        add_help=True
    )

    parser.add_argument("source", type=str, help="Source image", nargs="?", default="")
    parser.add_argument("target", type=str, help="Destination path", nargs="?", default="")
    parser.add_argument("preset", type=str, help="Which preset to be applied", nargs="?", default="")

    parser.add_argument("-l", "--list", action="store_true", default=False, help="Show a list of presets")
    parser.add_argument("-v", "--verbosity", action="store_true", default=False, help="Show more info on stdout")
    parser.add_argument("-q", "--quiet", action="store_true", default=False, help="Doesn't show anything on the stdout")

    args = parser.parse_args()

    return args.__dict__
