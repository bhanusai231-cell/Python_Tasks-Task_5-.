# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
arr = list(map(int, input().split()))

unique_scores = set(arr)
unique_scores.remove(max(unique_scores))

print(max(unique_scores))
