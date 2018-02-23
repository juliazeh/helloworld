#!/usr/bin/env python

import argparse
import helloworld


def parse_command_line():
    "parses args for the helloworld.py functions"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add short args
    parser.add_argument(
        "-m", "--militarytime",
        help="optional time to determine greeting",
        type=int)

    # add long args
    parser.add_argument(
        "--age",
        help="convert and return inputted age to age in dog years",
        type=int)

    # parse args
    args = parser.parse_args()
    return args


def main():
    "run helloworld on parsed args"
    args = parse_command_line()
    helloworld.helloworld(
        militarytime=args.militarytime,
        age=args.age)
