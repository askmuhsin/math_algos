import sys

num = None
if len(sys.argv)>1:
    num = int(sys.argv[1])

def fibonacci(num):
    if num<2:
        return num
    p, c = 0, 1
    while num>1:
        p, c = c, p+c
        num-=1
    return c

def main():
    print(fibonacci(num))

if __name__ == '__main__':
    main()
