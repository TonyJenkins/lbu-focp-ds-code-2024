#!/usr/bin/env python3

import sys

if __name__ == '__main__':

    try:
        with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2:
            print(f'{"Same" if f1.read() == f2.read() else "Different"}')

    except IndexError:
        print(f'Usage: {sys.argv[0]} <file1> <file2>')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open one of the files.')
