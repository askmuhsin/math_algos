#!/usr/bin/env python

import sys

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

a, b = None, None
if len(sys.argv)>2:
    if isInt(sys.argv[1]):
        a = int(sys.argv[1])
    if isInt(sys.argv[2]):
        b = int(sys.argv[2])

def gcd(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b

def main():
    gcd(a, b)
    # a, b = 1256, 288
    print("GCD of ({}, {}) is {}".format(a, b, gcd(a, b)))

if __name__ == '__main__':
    main()
