# Anagram
# https://www.hackerrank.com/challenges/anagram/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    count = 0

    for ch in set(s1):
        diff = s1.count(ch) - s2.count(ch)

        if diff > 0:
            count += diff

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
