#!/usr/bin/env python3
"""
Author : Emma Huffman <emmahuffman@email.arizona.edu>
Date   : 29 January 2020
Purpose: Python program to find position of a vowel within a word
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path


# --------------------------------------------------
def get_args():
    """Get arguments"""

    parser = argparse.ArgumentParser(
        description='Create Python argparse/simple program',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    defaults = get_defaults()

    parser.add_argument('program', help='Program name', type=str)

    parser.add_argument('-s',
                        '--simple',
                        help='Use simple format',
                        action='store_true')

    parser.add_argument('-n',
                        '--name',
                        type=str,
                        default=defaults.get('name', os.getenv('USER')),
                        help='Name for docstring')

    parser.add_argument('-e',
                        '--email',
                        type=str,
                        default=defaults.get('email', ''),
                        help='Email for docstring')

    parser.add_argument('-p',
                        '--purpose',
                        type=str,
                        default='Rock the Casbah',
                        help='Purpose for docstring')

    parser.add_argument('-f',
                        '--force',
                        help='Overwrite existing',
                        action='store_true')

    args = parser.parse_args()

    args.program = args.program.strip().replace('-', '_')

    if not args.program:
        parser.error('Not a usable filename "{}"'.format(args.program))

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    program = args.program

    if os.path.isfile(program) and not args.force:
        answer = input('"{}" exists.  Overwrite? [yN] '.format(program))
        if not answer.lower().startswith('y'):
            print('Will not overwrite. Bye!')
            sys.exit()

    header = preamble(name=args.name,
                      email=args.email,
                      purpose=args.purpose,
                      date=str(date.today()))
    text = simple() if args.simple else body(args.purpose)

    out_fh = open(program, 'w')
    out_fh.write(header + text)
    out_fh.close()
    subprocess.run(['chmod', '+x', program])
    print('Done, see new script "{}."'.format(program))

    vowel = 'a,e,i,o,u'
    if vowel in text:
        print(f("Found", vowel, "in text at index"))
        else print(vowel, "Not found in", text)


# --------------------------------------------------
def preamble(**args):
    return f"""#!/usr/bin/env python3
\"\"\"
Author : {args['name']}{' <' + args['email'] + '>' if args['email'] else ''}
Date   : {args['date']}
Purpose: {args['purpose']}
\"\"\"
"""


# --------------------------------------------------
def simple():
    return """
import os
import sys


# --------------------------------------------------
def main():
    \"\"\"Make a jazz noise here\"\"\"

    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    arg = args[0]

    print('Arg is "{}"'.format(arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
"""


# --------------------------------------------------
def body(purpose):
    text = """
import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    \"\"\"Get command-line arguments\"\"\"

    parser = argparse.ArgumentParser(
        description='{}',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='str',
                        help='Position of a vowel')
    parser.add_argument('text',
                        metavar='str',
                        help='Position of text')

    
    return parser.parse_args()


# --------------------------------------------------
def main():
    \"\"\"Make a jazz noise here\"\"\"

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional
    vowel = args.vowel
    text = args.text

    print('str_arg = "{{}}"'.format(str_arg))
    print('int_arg = "{{}}"'.format(int_arg))
    print('file_arg = "{{}}"'.format(file_arg.name if file_arg else ''))
    print('flag_arg = "{{}}"'.format(flag_arg))
    print('positional = "{{}}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
"""
    return text.format(purpose)


# --------------------------------------------------
def get_defaults():
    """Get defaults from ~/.new.py"""

    rc = os.path.join(str(Path.home()), '.new.py')
    defaults = {}
    if os.path.isfile(rc):
        for line in open(rc):
            match = re.match('([^=]+)=([^=]+)', line)
            if match:
                key, val = map(str.strip, match.groups())
                if key and val:
                    defaults[key] = val

    return defaults


# --------------------------------------------------
if __name__ == '__main__':
    main()
