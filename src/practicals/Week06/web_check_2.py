#!/usr/bin/env python3

import sys

from requests import get
from requests.exceptions import *

HTTP_SUCCESS = 200


if __name__ == '__main__':

    try:
        get(sys.argv[1]).raise_for_status()
        print(f'Web page at {sys.argv[1]} looks OK.')

    except HTTPError:
        print(f'No Web page at {sys.argv[1]}.')
    except ConnectionError:
        print('DNS Lookup Failed, or some other network issue.')
    except (InvalidURL, InvalidSchema, MissingSchema,):
        print('URL invalid or incorrect format.')
