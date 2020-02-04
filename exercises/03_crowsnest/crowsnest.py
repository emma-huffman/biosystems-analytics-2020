#!/usr/bin/env python3
"""
Author : emmahuffman
Date   : 2020-01-30
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

    parser.add_argument('word',
                        metavar='str',
                        help='A positional argument')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    descriptor = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f' Ahoy, Captain, {descriptor} {word} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
