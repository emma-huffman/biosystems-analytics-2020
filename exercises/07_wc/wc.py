#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 02/20/20
Purpose: Emulate wc (Word Count)
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('r'),
                        default=[sys.stdin],
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_chars, total_words = 0, 0, 0

    for fh in args.file:
        num_lines, num_chars, num_words = 0, 0, 0
        for line in fh:
            num_lines += 1
            num_chars += len(line)
            num_words += len(line.split())
        total_lines += num_lines
        total_chars += num_chars
        total_words += num_words
    print(f'{num_lines:8}{num_chars:8}{num_words:8} {fh.name}')

    if args.file > 1:
        print(f'{total_lines:8}{total_chars:8}{total_words:8} Total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
