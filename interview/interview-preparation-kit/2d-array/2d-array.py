#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

"""
https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


def hourglassSum(arr):

    hourglass = []

    for row in range(len(arr) - 2):
        for col in range(len(arr) - 2):
            hourglass.append(
                sum([sum(arr[row][col:col+3]),
                     arr[row+1][col+1],
                     sum(arr[row+2][col:col+3])]))
    return max(hourglass)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
