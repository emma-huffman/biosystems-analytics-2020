#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 03/22/2020
Purpose: Transcribing DNA to RNA
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribing DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='str',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input File(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir
    dna = args.FILE
    # rna = ''

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    trans = str.maketrans('T','U')
    dna = dna.translate(trans)

    for fh in args.file:
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        for line in fh:
            out_dir.write(dna)
    print(f'Done, wrote 1 sequence in 1 file to directory "out".')

    # for char in dna:
    #     rna = dna.replace('T', 'U')
    # print(rna)
    # for fh in args.file:
    #     out_file = os.path.join(out_dir, os.path.basename(fh.name))
    #     out_fh = open(out_file, 'wt')
    #     for line in fh:
    #         if i == 'T':
    #             rna += 'U'
    #         else:
    #             rna += i
#need to define i in some way so that I can iterate through lines.
#not sure how to set that parameter
        # for i in fh:
        #     if i == 'T':
        #         rna += 'U'
        #     else:
        #         rna += i

# two for loops
# need to iterate through line and through file
# take a lot from wc.py
# --------------------------------------------------
if __name__ == '__main__':
    main()
