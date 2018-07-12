#!/usr/bin/env python

import sys

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
    it=0
    if num_chk:
        num = int(num_chk)
        print("{} is".format(num), "prime" if isPrime(num) else "composite")
    # for i in range(101):
    #     print(i, " --> prime" if isPrime(i) else " --> composite")
    #     if isPrime(i):
    #         it+=1
    # print("counted {} primes".format(it))

if __name__=='__main__':
    main()
