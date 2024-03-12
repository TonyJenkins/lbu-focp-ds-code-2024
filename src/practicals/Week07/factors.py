#!/usr/bin/env python3


def factorise(num):
    return [f for f in range(1, num + 1) if num % f == 0]


def is_prime(num):
    return num > 1 and len(factorise(num)) == 2


if __name__ == '__main__':

    for x in range(10, 25):
        print(f'{x} -> {factorise(x)}')

    print()

    for x in range(1, 25):
        print(f'{x:2} -> {"Prime" if is_prime(x) else "Not Prime"}')
