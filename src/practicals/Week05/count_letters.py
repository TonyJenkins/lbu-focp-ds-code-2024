#!/usr/bin/env python3


def letter_types(s):
    return len([c for c in s if c.islower()]), len([c for c in s if c.isupper()])


if __name__ == '__main__':
    for a_string in ['Banana', 'banana', 'CHEESE', 'herrinG', 'Cheese%1427', '']:
        upper, lower = letter_types(a_string)
        print(f'{a_string} -> Lower {lower} Upper {upper}')
