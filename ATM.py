N = int(input())
P = list(map(int, input().split()))

P.sort()

accumulated_time = [P[0]]

for i, index in zip(P[1:], range(N)):
    accumulated_time.append(i + accumulated_time[index])

print(sum(accumulated_time))