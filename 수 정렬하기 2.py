import sys

N = int(input())

numbers = []

for i in range(N):
    numbers.append(sys.stdin.readline().rstrip())

numbers.sort()

for i in numbers:
    print(i)