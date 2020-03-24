#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 03/13/20
Purpose: Apples and Bananas
"""

import argparse
import os
import sys
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='Vowel to substitute',
                        metavar='str',
                        type=str,
                        choices='a''e''i''o''u',
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowel = args.vowel
    text = args.text

    for vow in 'aeiou':
        text = text.replace(vow, vowel)
        text = text.replace(vow.upper(), vowel.upper())

    print(text)

# --------------------------------------------------
if __name__ == '__main__':
    main()
