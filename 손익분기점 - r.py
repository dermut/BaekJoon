A, B, C = map(int, input().split())

breakeven_point = 0

if B >= C:
    breakeven_point = -1

else:
    breakeven_point = (A // (C - B)) + 1

print(breakeven_point)