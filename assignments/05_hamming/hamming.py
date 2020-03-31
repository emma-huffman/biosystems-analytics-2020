#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 03/02/2020
Purpose: Define differences in given text
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Define differences in given text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('r'))

    parser.add_argument('-m',
                        '--min',
                        help='Minimum distance to show',
                        metavar='int',
                        type=int,
                        default=0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file

    for line in args.file:
        word1, word2 = line.split()
        change = abs(len(word1)-len(word2))
        for char1, char2 in zip(word1, word2):
            if char1 != char2:
                change += 1
        if change >= args.min:
            print(f'{change:8}:{word1:20}{word2:20}')

    # for line in args.file:
    #     word1, word2 = line.rstrip().split()
    #
    #     l1, l2 = len(word1), len(word2)
    #     distance = abs(l1 - l2)
    #
    #     for i in range(min(l1, l2)):
    #         if word1[i] != word2[i]:
    #             distance += 1
    #
    # if distance >= args.min:
    #     print(f'{distance:8}:{word1:20}{word2:20}')

    


















    # for line in args.file:
    #     word1, word2 = line.split()
    #     n_change = abs(len(word1) - len(word2))
    #     for char1, char2 in zip(word1, word2):
    #         if char1 != char2:
    #             n_change += 1
    #     if n_change >= args.min:
    #         print(f'{n_change:8}:{word1:20}{word2:20}')















    # for line in args.file:
    #     word1, word2 = line.split()
    #     n_change = abs(len(word1) - len(word2))
    #     for char1, char2 in zip(word1, word2):
    #         if char1 != char2:
    #             n_change += 1
    #     if n_change >= args.min:
    #         print(f'{n_change:8}:{word1:20}{word2:20}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
