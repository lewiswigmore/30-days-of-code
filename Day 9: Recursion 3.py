#!/bin/python3

import math
import os
import random
import re
import sys

# Interation
def iterativeFactorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
    
# Recursion
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
