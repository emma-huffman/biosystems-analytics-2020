#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
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
                        nargs='?',
                        type=argparse.FileType('r'))

    args = parser.parse_args()
    if not args.num > 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    with open(args.file) as file:
        for x in range(args.num):
            head = file.read()
        print(head)
# --------------------------------------------------
if __name__ == '__main__':
    main()
