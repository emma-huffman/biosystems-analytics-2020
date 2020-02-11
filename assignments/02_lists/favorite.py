#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu
Date   : 02/09/2020
Purpose: Print my favorite things
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='My Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Some things')

    parser.add_argument('-s',
                        '--sep',
                        help='A separator',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    item = args.item
    sep_arg = args.sep
    num = len(item)

    if num == 1:
        favorite = item[0]
        print(f'{item[0]}')
        print('This is one of my favorite things.')
    elif num == 2:
        favorite = ',' .join(item)
        print(f'{item[0]}, {item[1]}')
        print('These are a few of my favorite things.')
    else:
        item[-1] = 'and ' + item[-1]
        favorite = ', ' .join(item)
        print(f'{item[0]}, {item[1]}, {item[-1]}')
        print('These are a few of my favorite things.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
