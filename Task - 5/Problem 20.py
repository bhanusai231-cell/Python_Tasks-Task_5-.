# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem
def pile_up(blocks):
    while len(blocks) > 1:
        if blocks[0] >= blocks[-1]:
            if blocks[0] < blocks[-2]:
                return "No"
            blocks.pop(0)
        else:
            if blocks[-1] < blocks[1]:
                return "No"
            blocks.pop()

    return "Yes"


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        blocks = list(map(int, input().split()))

        print(pile_up(blocks))
