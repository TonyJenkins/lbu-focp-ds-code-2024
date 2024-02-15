#!/usr/bin/env python3

if __name__ == '__main__':
    name = input('Hello, what is your name? ')

    year_now = int(input('What year is it today? '))
    year_born = int(input('And what year were you born? '))

    print(f'Hello, {name}. It is good to meet you. This year you will '
          f'be {year_now - year_born} years old.')
