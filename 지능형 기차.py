up, down = [], []

for i in range(4):
    tmp1, tmp2 = map(int, input().split())
    up.append(tmp1), down.append(tmp2)

index = 0
largest_number = 0

for i in range(4):
    index += down[i] - up[i]
    if index >= largest_number:
        largest_number = index
    else:
        pass

print(largest_number)