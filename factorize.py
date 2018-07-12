#!/usr/bin/env python

import sys
from math import inf

num_chk = None
if len(sys.argv)>1:
    num_chk = sys.argv[1]

n=int(num_chk)

def factorize(n):
    factors = []
    i=1
    while(i<=n):
        k=0
        if(n%i==0):
            j=1
            while(j<=i):
                if(i%j==0):
                    k=k+1
                j=j+1
            if(k==2):
                factors.append(i)
        i=i+1
    return factors

def main():
    print("Factors of {} are : \n{}".format(n, factorize(n)))

if __name__ == '__main__':
    main()
