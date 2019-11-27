A, B, V = map(int, input().split())

days = (V // (A - B)) - 1

print(days)