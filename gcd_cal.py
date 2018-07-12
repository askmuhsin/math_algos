def gcd(a, b):
    while a % b != 0:
        a, b = b, a%b
    return b

def main():
    a, b = 1256, 288
    print("GCD of ({}, {}) is {}".format(a, b, gcd(a, b)))

if __name__ == '__main__':
    main()
