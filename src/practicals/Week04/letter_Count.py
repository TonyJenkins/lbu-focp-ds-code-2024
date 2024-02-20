#!/usr/bin/env python3


def letter_count(s):
    upper = len([c for c in s if c.isupper()])
    lower = len([c for c in s if c.islower()])

    return upper, lower


if __name__ == '__main__':
    for a_string in ['A', 'a', 'Cheese', 'chEEse', 'cheeeeeesE']:
        print(f'{a_string:12} -> {letter_count(a_string)[0]} : {letter_count(a_string)[1]}')
