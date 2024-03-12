#!/usr/bin/env python3

from string import ascii_lowercase as letters
from random import choice, randint


def random_letter():
    return choice(letters)


def n_random_letters(n):
    return ''.join(random_letter() for count in range(n))


def encrypt(message):
    spacing = randint(2, 20)

    encrypted = ''

    for letter in message:
        encrypted += letter + n_random_letters(spacing)

    return encrypted, spacing


def decrypt(message, spacing):
    return message[::spacing + 1]


if __name__ == '__main__':
    m = 'send cheese'

    encrypted_message, spacing_used = encrypt(m)

    print(f'"{m}" -> "{encrypted_message}", spacing {spacing_used}')
    print(f'"{decrypt(encrypted_message, spacing_used)}"')
