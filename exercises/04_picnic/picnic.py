#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu
Date   : 02/11/2020
Purpose: Determine what items you're bringing to the picnic
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Food',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='What we will eat')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the Items')

    return parser.parse_args()


# --------------------------------------------------

# --------------------------------------------------
if __name__ == '__main__':
    main()
