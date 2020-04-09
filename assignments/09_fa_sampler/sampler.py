#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 04/7/20
Purpose: Probabalistically subset FASTA files
"""

import argparse
import os
import sys
import random
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabalistically subset FASTA filesq',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input FASTA file(s)')

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default='out')

    args = parser.parse_args()

    if not 0 <= args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    num_seqs = 0
    for i, fh in enumerate(args.file, start=1):
        basename = os.path.basename(fh.name)
        out_file = os.path.join(out_dir, basename)
        out_fh = open(out_file, 'wt')
        print(f'{i:3}: {basename}')

        for rec in SeqIO.parse(fh, 'fasta'):
            if random.random() <= args.pct:
                num_seqs += 1
                SeqIO.write(rec, out_fh, 'fasta')

        print(num_seqs)


    # for fh in args.file:
    #     out_file = os.path.join(out_dir, os.path.basename(fh.name))
    #     out_fh = open(out_file, 'wt')
    #     num_files += 1

    #print number of files in a counted order
    # for i, line in enumerate(args.file, start=1):
    #     print(line, end='')
    #     if i == num_files:
    #         break
    #
    # #print exit statement
    # print(f'Wrote {num_seq} sequence{"" if num_seq == 1 else "s"} '
    #       f'in {files} file{"" if files == 1 else "s"}'
    #       f'to directory "{out_dir}".'
    #       f'in {files} file{"" if files == 1 else "s"}')



    # for fh, line in enumerate(args.file, start=1):
    #     basename = os.path.basename(fh.name)
    #     out_file = os.path.join(args.outdir, basename)
    #     print(line, end='')
    #     if line == num_files:
    #         break
    #
    #     out_fh = open(out_file, 'wt')
    #     for rec in SeqIO.parse(fh, 'fasta'):
    #         # if random.random(range(args.pct)):   ?
    #             SeqIO.write(rec, out_fh, 'fasta')
    #
    #     out_fh.close()
    #
    # print((f'Wrote {num_seq} sequence{"" if num_seq == 1 else "s"} '
    #       f'in {num_files} file{"" if num_files == 1 else "s"}'
    #       f'to directory "{out_dir}".'
    #       f'in {num_files} file{"" if num_files == 1 else "s"}'))






# --------------------------------------------------
if __name__ == '__main__':
    main()
