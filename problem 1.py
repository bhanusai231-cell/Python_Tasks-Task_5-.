# Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
english = set(map(int,input().split()))

n = int(input())
french = set(map(int,input().split()))
result = english.symmetric_difference(french)

print(len(result))
 
