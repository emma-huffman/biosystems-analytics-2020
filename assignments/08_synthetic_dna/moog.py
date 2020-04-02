#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import random
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        type=argparse.FileType('wt'),
                        metavar='str',
                        help='Output filename',
                        default='out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        default='dna',
                        choices=['dna', 'rna'])

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        metavar='float',
                        type=float,
                        help='Percent GC',
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        type=int,
                        help='Random seed',
                        default=None)

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    if os.path.isfile(args.outfile):
        os.remove(args.outfile)

    for n in args.numseqs:
        seq_len = random.randint(range(args.minlen, args.maxlen))
        seq = str(random.sample(seq_len, pool))
        args.outfile.write(seq + '.fasta')

    print(f'Done, wrote {args.numseqs} DNA sequences to "{args.outfile}".')


# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """ Create the Pool of Bases"""
    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_at = int(((1 - pctgc) / 2) * max_len)
    num_gc = int((pctgc / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + 't_or_u' * num_at


# --------------------------------------------------
if __name__ == '__main__':
    main()
