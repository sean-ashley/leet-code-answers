#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i =0
    num_jumps = 0
    #loop thru list
    while i < len(c)-1:
        #try and except to make sure we arnt on the second last element
        try:
            #if there isnt a thunderhead two away, do a big jump
            if c[i+2] == 0:
                i += 2
                num_jumps += 1
            #otherwise do a small jump
            else:
                i+=1
                num_jumps += 1
        #if we are on the sec
        except IndexError:
            
            num_jumps +=1
            return num_jumps
    return num_jumps
                
                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
