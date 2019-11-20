X = int(input())

count_operation = 0

if ((X - 1) % 9) == 0:
    X -= 1
    count_operation += 1

while X > 1:
    if (X % 3) == 0:
        X = X / 3
    elif (X % 2) == 0:
        X = X / 2
    else:
        X = X - 1

    count_operation += 1

print(count_operation)