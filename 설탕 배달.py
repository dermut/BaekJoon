N = int(input())

count_3, count_5 = 0, 0

result = 0

count_5 = N // 5
count_3 = (N - (count_5 * 5)) // 3

if ((count_5 * 5) + (count_3 * 3)) == N:
    result = count_3 + count_5
else:
    result = -1
    

print(result)