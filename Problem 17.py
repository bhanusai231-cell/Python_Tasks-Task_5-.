# Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    for length in range(1, len(s) // 2 + 1):
        first = int(s[:length])
        current = first
        built = ""

        while len(built) < len(s):
            built += str(current)
            current += 1

        if built == s:
            print("YES", first)
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
