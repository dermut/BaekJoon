N = int(input())
N_numbers = list(map(int, input().split()))

M = int(input())
M_numbers = list(map(int, input().split()))

cache = [0] * 100001

for i in N_numbers:
    cache[i] = 1

for i in M_numbers:
    if cache[i] == 1:
        print(1)
    else:
        print(0)