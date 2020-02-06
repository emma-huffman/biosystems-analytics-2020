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
        description='Find position of vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='vowel',
                        help='A vowel to look for')
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


    print('vowel_arg = "{}"'.format(vowel_arg))
    print('text_arg = "{}"'.format(text_arg))
    print('int_arg = "{}"'.format(int_arg))
    print('file_arg = "{}"'.format(file_arg.name))
    print('flag_arg = "{}"'.format(flag_arg))
    print('positional = "{}"'.format(pos_arg))

    y = input("Enter a word:  ")
    for i in range(len(y)):
        if (y[i] == "a"):
            x=i+1
            print("Found",y[i], "at position", x)
        if (y[i] == "e"):
            x=i+1
            print("Found",y[i], "at position", x)
        if (y[i] == "i"):
            x=i+1
            print("Found",y[i], "at position", x)
        if (y[i] == "o"):
            x=i+1
            print("Found",y[i], "at position", x)
        if (y[i] == "u"):
            x=i+1
            print("Found",y[i], "at position", x)


# --------------------------------------------------
if __name__ == '__main__':

    main()
