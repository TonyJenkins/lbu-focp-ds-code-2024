#!/usr/bin/env python3

def obfuscate(message):
    return ''.join(c for c in message[::-1].replace(' ', ''))


if __name__ == '__main__':
    m = 'send cheese'

    print(f'"{m}" -> "{obfuscate(m)}"')
