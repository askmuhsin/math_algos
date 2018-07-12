from gcd_cal import gcd

def pollardRho(num):
    x_fixed = 2
    cycle_size = 2
    x = 2
    factor = 1

    while factor==1:
        count = 1
        while count <= cycle_size and factor <=1:
            x = (x*x + 1)%num
            factor = gcd(x - x_fixed, num)
            count+=1
        cycle_size *= 2
        x_fixed = x

    return factor

def main():
    num = 123
    print("Factors of {} --> {}".format(num, pollardRho(num)))

if __name__ == '__main__':
    main()
