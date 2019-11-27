import math

T = int(input())

result = []

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # 일치하는 경우
    if x1 == x2 and y1 == y2 and r1 == r2:
        result.append(-1)

    # 두 점에서 만나는 경우
    elif r1 + r2 > distance > abs(r1 - r2):
        result.append(2)

    # 한 점에서 만나는 경우, 내접, 외접
    elif r1 + r2 == distance:
        result.append(1)

    elif abs(r1 - r2) == distance:
        result.append(1)

    # 만나지 않는 경우, 외부에 있을 때, 내부에 있을 때
    else:
        result.append(0)

for i in result:
    print(i)