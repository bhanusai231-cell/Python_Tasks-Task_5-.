# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    from collections import Counter

    freq = Counter(s)

    for ch in list(freq.keys()):
        freq[ch] -= 1

        if freq[ch] == 0:
            del freq[ch]

        if len(set(freq.values())) == 1:
            return "YES"

        freq = Counter(s)

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
