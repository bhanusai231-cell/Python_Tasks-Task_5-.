# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem
a = int(input())
rooms = list(map(int,input().split()))

for room in set(rooms):
    if rooms.count(room)==1:
        print(room)
        break
