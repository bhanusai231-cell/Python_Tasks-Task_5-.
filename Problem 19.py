# Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()

    current = 0
    prev = ''

    for ch in s:
        if ch == prev:
            current += ord(ch) - ord('a') + 1
        else:
            current = ord(ch) - ord('a') + 1
            prev = ch

        weights.add(current)

    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
