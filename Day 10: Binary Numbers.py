#!/bin/python3

import math
import os
import random
import re
import sys


    

if __name__ == '__main__':
    n = int(input().strip())
    # Convert to binary string
    b = bin(n)[2::]
    
    # Convert string to list
    lst = []
    for i in b:
        lst.append(i)
    
    # Iterate through list to find highest count of consecutive 1s
    max_length = 0
    current_length = 0
    
    for j in lst:
        if j == "1":
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    print(max_length)
    
