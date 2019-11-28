N = int(input())

count_3, count_5 = 0, 0

result = 0

while N > 1:    
    if N % 5 == 0:
        count_5 = N // 5
        result += count_5
        N -= (count_5 * 5)
        print(N)
    elif N % 3 == 0:
        count_3 = N // 3
        result += count_3
        N -= (count_3 * 3)
        print(N)
    elif N < 5:
        result = -1
        break
    else:
        result += 1
        N -= 5
        print(N)
        continue

print(result)
