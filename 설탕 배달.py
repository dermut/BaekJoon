N = int(input())

# 15로 나눌 수 있는 것 먼저 센다.
count_15 = 0

count_3, count_5 = 0, 0

result = 0

if N >= 15:
    count_15 = N // 15
    count_5 = count_15 * 3
    N -= (count_15 * 15)

