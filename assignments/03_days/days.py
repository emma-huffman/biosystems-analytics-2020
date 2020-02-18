#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 20 February 2020
Purpose: What to do on each day
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='What to do on each day',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('day',
                        metavar='str',
                        nargs='+',
                        type=str,
                        choices='Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday',
                        help='Days of the week')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    day = args.day

    feeling = {'Monday': 'On Mondays I never go to work',
           'Tuesday': 'On Tuesdays I stay at home',
           'Wednesday': 'On Wednesdays I never feel inclined',
           'Thursday': "On Thursdays, it's a holiday",
           'Friday': 'And Fridays I detest',
           'Saturday': "Oh, it's much too late on a Saturday",
            'Sunday': 'And Sunday is the day of rest'}

    try:
        for char in args.day:
            print(feeling.get(char, char))
    except (KeyError):
        print("Can't find", char)











# --------------------------------------------------
if __name__ == '__main__':
    main()
