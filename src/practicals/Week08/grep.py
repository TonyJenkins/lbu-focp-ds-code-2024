#!/usr/bin/env python3

import sys


if __name__ == '__main__':

    try:
        file_to_search = sys.argv[2]
        pattern = sys.argv[1]

        with open(file_to_search, 'r') as infile:
            for line in infile:
                if pattern in line:
                    print(line, end='')

    except IndexError:
        print(f'Usage: {sys.argv[0]} <pattern> <file>')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open the file.')
