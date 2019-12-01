side1, side2, side3 = 1, 1, 1

result = []

while side1 != 0 or side2 != 0 or side3 != 0:
    tmp = list(map(int, input().split()))

    tmp.sort()

    if (tmp[2] ** 2) == (tmp[0] ** 2) + (tmp[1] ** 2):
        result.append("right")
    else:
        result.append("wrong")

    side1 = tmp[0]
    side2 = tmp[1]
    side3 = tmp[2]


for i in result[:-1]:
    print(i)