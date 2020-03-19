#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 03/13/2020
Purpose: Translate DNA/RNA to proteins
"""

import argparse
import os
import sys
import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA/RNA sequence')


    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    str = args.str.upper()
    codons = {}

    for line in args.codons:
        codon, protein = line.upper().split()
        codons[codon] = protein

    k = 3
    proteins = []
    for codon in [str[i:i + k] for i in range(0, len(str) - k + 1, k)]:
        proteins.append(codons.get(codon, '-'))

    print(''.join(proteins), file=args.outfile)

    print(f'Output written to "{args.outfile.name}".')
    # print(''.join(proteins), file=open(args.outfile, 'wt'))
    #
    # out_fh = open(args.outfile, 'wt')
    # out_fh.write(''.join(proteins))
    # out_fh.close()
# --------------------------------------------------
if __name__ == '__main__':
    main()
