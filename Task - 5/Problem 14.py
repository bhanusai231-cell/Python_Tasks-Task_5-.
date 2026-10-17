# Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input())

student_marks = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

student = input()

average = sum(student_marks[student]) / len(student_marks[student])

print(f"{average:.2f}")
