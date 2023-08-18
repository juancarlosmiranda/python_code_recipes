"""
Project:
Author: Juan Carlos Miranda
Date:
Description:
 Testing command line example of https://docs.python.org/3/howto/argparse.html

Use:
"""
from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(description="Text description of the command")
    parser.add_argument("FILE", type=str, help="Path to a file")
    parser.add_argument("--device", type=int, help="Device ID", default=0)
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

    args = parser.parse_args()

    print("args.FILE=", args.FILE)
    print("args.device=", args.device)

    if args.verbose:
        print("defined verbose", args.verbose)