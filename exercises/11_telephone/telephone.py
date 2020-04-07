#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 04/07/20
Purpose: Play telephone through randomly mutated strings
"""

import argparse
import random
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mutate a string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random seed value',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if not 0 <= args.mutations < 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = args.text
    alpha = string.ascii_letters + string.punctuation
    len_text = len(text)
    num_mutations = round(len(text) * args.mutations)
    new_text = text
    # for char in text:
    #     new_text += random.choice(alpha) if random.random() <= args.mutations else char
    indexes = random.sample(range(len(text)), num_mutations)
    for i in indexes:
        new_char = random.choice(alpha.replace(new_text[i], ''))
        new_text = new_text[:i] + new_char + new_text[i + 1:]
    print(f'You said: "{text}"')
    print(f'I heard : "{new_text}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
