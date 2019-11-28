ten = int(input())

cars = map(int, input().split())

result = 0

for i in cars:
    if i == ten:
        result += 1

print(result)