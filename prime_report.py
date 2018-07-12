import sys
import is_prime
import nearestPrime
import os

num = None
if len(sys.argv)>0:
    num = int(sys.argv[1])

def main():
    if num:
        if is_prime.isPrime(num):
            print("{} is prime!".format(num))
        else:
            print("{} is composite".format(num))
            print("Factors of {} are : ".format(num))
            cmd = "factor " + str(num)
            print(os.system(cmd))
    print(nearestPrime.main())


if __name__ == '__main__':
    main()
