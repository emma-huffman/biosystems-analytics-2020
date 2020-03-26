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

    parser.add_argument('file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input File(s)')

    parser.add_argument('-o',
                        '--outdir',
                        metavar='DIR',
                        help='Output directory',
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    trans = str.maketrans('T', 'U')

    num_files, num_seqs = 0, 0
    for fh in args.file:
        num_files += 1
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')

        for dna in fh:
            num_seqs += 1
            rna = dna.translate(trans)
            out_fh.write(rna + '\n')

        out_fh.close()

        print(f'Done, wrote {num_seqs} sequence{"" if num_seqs == 1 else "s"} '
              f'in {num_files} file{"" if num_files == 1 else "s"} '
              f'to directory "{out_dir}".')


# two for loops
# need to iterate through line and through file
# take a lot from wc.py
# --------------------------------------------------
if __name__ == '__main__':
    main()
