#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 02/05/2020
Purpose: Determine the position of a vowel in text
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find position of vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='vowel',
                        help='A vowel to look for',
                        choices='aeiouAEIOU')

    parser.add_argument('text',
                        metavar='text',
                        help='The text to search')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = args.text

    if vowel in text:
        index = text.index(vowel)
        print(f'Found "{vowel}" in "{text}" at index {index}.')
    else:
        print(f'"{vowel}" is not found in "{text}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
