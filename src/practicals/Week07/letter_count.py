#!/usr/bin/env python3

from operator import itemgetter
from string import ascii_lowercase as letters


if __name__ == '__main__':

    counts = {
        letter: 0 for letter in letters
    }

    message = input('Enter the message: ')

    for character in message.lower():
        if character in letters:
            counts[character] += 1

    most_common = sorted(counts.items(), key=itemgetter(1), reverse=True)[:5]

    for letter in most_common:
        print(letter[0], letter[1])
