#!/usr/bin/env python

import sys

num_chk = None
if len(sys.argv)>1:
    num_chk = sys.argv[1]

def maxAndMin(num):
    max = 0
    min = 0
    num_cp = str(num)
    num_lst = [n for n in num_cp]

    num_lst_max = sorted(num_lst)
    num_lst_min = sorted(num_lst, reverse=True)

    for n in range(len(num_lst_max)):
        temp = int(num_lst_max[n]) * 10**n
        max+=temp

    for n in range(len(num_lst_min)):
        temp = int(num_lst_min[n]) * 10**n
        min+=temp

    return max, min

def kaprekarOp(num):
    seq = True
    sub = num
    while seq:
        mx, mn = maxAndMin(sub)
        subprev = sub
        sub = mx - mn
        if sub==subprev:
            seq = False
        print("{} - {} = {}".format(mx, mn, sub))

def main():
    if num_chk:
        num = int(num_chk)
        kaprekarOp(num)

if __name__=='__main__':
    main()
