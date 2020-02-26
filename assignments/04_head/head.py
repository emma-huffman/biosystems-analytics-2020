#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of lines',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('file',
                        help='Input File',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = open(args.file, 'rt') if args.file else sys.stdout
    num_lines = args.num
    if num_lines != 0:
        for fh in args.file:
            len(args.file.splitlines())
    else:
        print(sys.stderr)

# --------------------------------------------------
if __name__ == '__main__':
    main()
