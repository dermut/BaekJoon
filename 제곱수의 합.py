import math
N = int(input())

base = math.floor(math.sqrt(N))
counts = 0
index = 0
print(base)

while N > 0:
    index += 1
    print(base, index, N, counts)
    if N == 1:
        counts += 1
        break
    elif N - (base ** 2) < 0:
        base -= 1
        continue
    else:
        N -= (base ** 2)
        counts += 1


print(counts)