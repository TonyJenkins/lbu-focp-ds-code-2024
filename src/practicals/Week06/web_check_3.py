#!/usr/bin/env python3

import sys

from requests import get

HTTP_SUCCESS = 200


if __name__ == '__main__':

    try:
        code = get(sys.argv[1]).status_code
        if code == 200:
            print(f'Web page at {sys.argv[1]} looks OK.')
        else:
            print(f'Web page at {sys.argv[1]} cannot be accessed.')
    except:
        print('No web site found')
