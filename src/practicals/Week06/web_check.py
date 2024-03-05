#!/usr/bin/env python3

from sys import argv
from urllib.error import URLError
from urllib.request import urlopen, HTTPError

if __name__ == '__main__':

    try:
        response = urlopen(argv[1])
        print(f'Web page at {argv[1]} looks OK.')
    except IndexError:
        print('No URL on the command line to check.')
    except ValueError:
        print('Incorrect format for URL. Did you miss the "https://"?')
    except HTTPError:
        print('No web page found at that location.')
    except URLError:
        print('DNS failed. Or some other network woes.')
