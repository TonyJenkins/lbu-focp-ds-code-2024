#!/usr/bin/env python3

def test_number(num):
    return 0 <= num <= 100


if __name__ == '__main__':

    for i in range (90, 110):
        print(f'{i:3} : {"In" if test_number(i) else "Out of"} Range')
