#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import string
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='Word to Rhyme')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    start, rest = stemmer(args.word)
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh '
        'wr sch scr shr sph spl spr squ str thr').split()

    if rest:
        print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
        # print('rhymes here')
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
def stemmer(word):
    """Break a word into start, rest"""

    vowels = 'aeiou'
    consonants = ''.join(
        [c for c in string.ascii_lowercase if c not in 'aeiou'])

    pattern = f'([{consonants}]+)?([aeiou].*)'
    # match = re.match(pattern, word)

    # pattern = (
    #             '('  # capture group 1
    #             '[' + consonants + ']'  # Character class
    #             '+'  # One or more
    #             ')'  # End of capture
    #             '?'  # Optional
    #             '('  # Capture group 2
    #             '[aeiou]'  # Class of vowels
    #             '.*'  # zero or more of anything
    #             ')'  # End capture 2
    #            )

    match = re.match(pattern, word.lower())

    return (match.group(1) or '', match.group(2) or '') if match else ('', '')


# --------------------------------------------------
def test_stemmer():
    """Test"""

    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('apple') == ('', 'apple')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('rdnzl') == ('rdnzl', '')
    assert stemmer('RDNZL') == ('rdnzl', '')


# --------------------------------------------------
if __name__ == '__main__':
    main()
