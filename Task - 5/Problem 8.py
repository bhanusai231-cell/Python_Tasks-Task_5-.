# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countries = set()
for i in range (n):
    country = input()
    countries.add(country)
print(len(countries))
