#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 3/30/20
Purpose: Heap Abuse
"""

import argparse
import os
import parser
import sys
import random

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap Abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='Number of Insults',
                        metavar='insults',
                        type=int,
                        default=3)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random Seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error('--adjectives "{}" must be > 0'.format(args.adjectives))

    if args.number < 1:
        parser.error('--number "{}" must be > 0'.format(args.number))


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)


    adjectives = "bankrupt base caterwauling corrupt cullionly detestable dishonest false" \
                 " filthsome filthy foolish foul gross heedless indistinguishable infected" \
                 " insatiate irksome lascivious lecherous loathsome lubbery old peevish" \
                 " rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced" \
                 " toad-spotted unmannered vile wall-eyed".strip().split()

    nouns = "Judan Satan ape ass barbermonger beggar block boy braggart butt carbuncle" \
            " coward coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack" \
            " jolthead knave liar lunatic maw milksop minion ratcatcher recreant rogue scold" \
            " slave swine traitor varlet villain worm".strip().split()

    for n in range(args.number):
        adj = ', '.join(random.sample(adjectives, k=args.adjectives))
        print(f'You {adj} {random.choice(nouns)}!')


    return args
# --------------------------------------------------
if __name__ == '__main__':
    main()
