# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
def print_rangoli(size):
    lines = []

    for i in range(size):
        left = []

        for j in range(size - 1, i - 1, -1):
            left.append(chr(97 + j))

        right = left[-2::-1]
        row = "-".join(left + right)
        lines.append(row.center(4 * size - 3, "-"))

    print("\n".join(lines[::-1] + lines[1:]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
