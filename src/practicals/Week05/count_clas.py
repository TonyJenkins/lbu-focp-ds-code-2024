#!/usr/bin/env python3


import sys


if __name__ == '__main__':

    clas = len(sys.argv) - 1
    print(f'There {"was" if clas == 1 else "were"} {clas} '
          f'argument{"" if clas == 1 else "s"} on the line.')
