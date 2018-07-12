#!/usr/bin/env python

import sys
from math import inf

num_chk = None
if len(sys.argv)>1:
    num_chk = sys.argv[1]

def isPrime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    for n in range(5, int(num**0.5)+1, 6):
        if num%n==0 or num%(n+2)==0:
            return False
    return True


def main():
    if num_chk:
        num = int(num_chk)
        diff_prev = num
        younger_prime = 2
        for n in range(2, num):
            if isPrime(n):
                diff = num - n
                if diff<diff_prev:
                    younger_prime = n
                    diff_prev = diff
        print("Nearest prime number lesser than {} \t--> {}".format(num, younger_prime))

        older_prime = None
        n = num+1
        while not older_prime:
            if isPrime(n):
                older_prime=n
            n+=1

        print("Nearest prime number greater than {} \t--> {}".format(num, older_prime))


if __name__ == '__main__':
    main()
