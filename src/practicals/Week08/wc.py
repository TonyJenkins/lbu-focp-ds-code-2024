#!/usr/bin/env python3

import sys


if __name__ == '__main__':

    try:
        file_to_search = sys.argv[1]

        characters = 0
        words = 0
        lines = 0

        with open(file_to_search, 'r') as infile:
            for line in infile:
                lines += 1
                characters += len(line) - 1
                words += len(line.split())

        print(f'Characters: {characters}')
        print(f'Words:       {words}')
        print(f'Lines:       {lines}')

    except IndexError:
        print(f'Usage: {sys.argv[0]} <file>')
    except FileNotFoundError:
        print(f'{sys.argv[0]}: Cannot open the file.')
