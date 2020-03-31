#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import io
import os
import sys


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
                        type=argparse.FileType('r'))

    args = parser.parse_args()
    if not args.num > 0:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.file:
        print(fh.name)
        num_line = 0
        for line in fh:
            num_line += 1
            print(line, end='')
            if num_line == args.num:
                break

# --------------------------------------------------
if __name__ == '__main__':
    main()
