import argparse


def parse_args() -> dict:
    parser = argparse.ArgumentParser(
        description="A CLI tool which applies filters to photos",
        add_help=True
    )

    parser.add_argument("source", type=str)
    parser.add_argument("target", type=str)
    parser.add_argument("preset", type=str)

    parser.add_argument("--color", type=float, default=1.0)
    parser.add_argument("--contrast", type=float, default=1.0)

    args = parser.parse_args()

    return args.__dict__
