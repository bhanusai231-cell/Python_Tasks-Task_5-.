# Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    from collections import Counter

    freq = Counter(s)

    odd = 0

    for count in freq.values():
        if count % 2 != 0:
            odd += 1

    if odd <= 1:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
