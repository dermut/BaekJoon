N = int(input())

result = 1
count_6 = 6

index = 1

while index < N:
    index += count_6

    result += 1
    count_6 = 6 * result

print(result)