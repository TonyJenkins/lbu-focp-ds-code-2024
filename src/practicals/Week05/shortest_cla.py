#!/usr/bin/env python3


import sys


def shortest_string(string_list):
    string_list.sort(key=len)

    return string_list[0]


if __name__ == '__main__':
    try:
        print(f'Shortest CLA: {shortest_string(sys.argv[1:])}')
    except IndexError:
        print('No CLAs provided.')
