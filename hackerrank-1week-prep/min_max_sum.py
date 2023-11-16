# Given five positive integers, find the minimumimum and maximumimum values that can be calculated by summinimumg exactly four of the five integers. Then print the respective minimumimum and maximumimum values as a single line of two space-separated long integers.

# Example

# The minimumimum sum is  and the maximumimum sum is . The function prints

# 16 24
# Function Description

# Complete the minimumimaximumSum function in the editor below.

# minimumimaximumSum has the following parameter(s):

# arr: an array of  integers
# Print

# Print two space-separated integers on one line: the minimumimum sum and the maximumimum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.

# Constraints


# Output Format

# Print two space-separated long integers denoting the respective minimumimum and maximumimum values that can be calculated by summinimumg exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14
# Explanation

# The numbers are , , , , and . Calculate the following sums using four of the five integers:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumimaximumSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumimaximumSum(arr):
    # Write your code here
    minimum = sys.maxsize
    maximum = 0
    total = 0

    for num in arr:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    print(total-maximum, total-minimum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    minimumimaximumSum(arr)
