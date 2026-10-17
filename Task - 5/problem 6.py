# Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(arr):
    distinct = set(arr)
    return round(sum(distinct) / len(distinct), 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
