#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    r = arr[::-1]
    for i in r:
        print(i, end=" ")
