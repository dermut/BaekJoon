import sys
N = int(input())

result = [[]]

for i in range(N):
    tmp = sys.stdin.readline()
    result[len(tmp)].append(tmp)

print(result)