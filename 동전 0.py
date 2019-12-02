N, K = map(int, input().split())

coins = []
counts = 0

for i in range(N):
    coins.append(int(input()))

for i in range(N - 1, 0, -1):
    if K > coins[i]:
        counts += (K // coins[i])
        K -= (coins[i]) * (K // coins[i])

print(counts)