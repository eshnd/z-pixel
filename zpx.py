#!/bin/python

import argparse

p = argparse.ArgumentParser(description="Scales pixel art without blur, making all sprites share the same pixel size")

p.add_argument(
    "-f", "--files",
    nargs="+",
    help="File(s) to scale"
)
p.add_argument("-s", "--size", type=float, help="Size % to scale images to")

args = p.parse_args() # creates args.files and args.size

