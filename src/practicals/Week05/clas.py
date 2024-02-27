#!/usr/bin/env python3


import sys


if __name__ == '__main__':

    try:
        f = open(sys.argv[1])
        print(len(f.readlines()))
    except FileNotFoundError:
        print(f'{sys.argv[0][2:]}: File does not exist.')
    except IndexError:
        print(f'{sys.argv[0][2:]}: No file name on the command-line.')
