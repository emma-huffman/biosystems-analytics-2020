#!/usr/bin/env python3
"""
Author : Emma Huffman
Date   : 4/30/20
Purpose: Filter swissprot file for keywords, taxa
"""

import argparse
import os
import sys
import io


# --------------------------------------------------
from Bio import SeqIO


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        help='Swissprot file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keywords to take',
                        metavar='keyword',
                        type=str,
                        default='')

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='taxa to skip',
                        metavar='taxa',
                        nargs='*',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=str,
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    wanted_kw = set(map(str.lower, args.keyword))
    skip_taxa = set(map(str.lower, args.skiptaxa or []))
    num_taken, num_skipped = 0, 0
    for rec in SeqIO.parse(args.file, 'swiss'):
        annots = rec.annotations

        taxa = annots.get('taxonomy')
        if taxa:
            taxa = set(map(str.lower, taxa))
            if skip_taxa.intersection(taxa):
                num_skipped += 1
                continue

        keywords = annots.get('keywords')
        if keywords:
            keywords = set(map(str.lower, keywords))
            if wanted_kw.intersection(keywords):
                num_taken += 1
                SeqIO.write(rec, args.outfile, 'fasta-2line')

        break

    print(f'Done, see output in "{args.outfile.name}".')
    print(f'Done, skipped {num_skipped} ant took {num_taken}. See outout in "{args.outfile.name}".')
# --------------------------------------------------
if __name__ == '__main__':
    main()
