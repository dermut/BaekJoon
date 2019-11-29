A, B, C = map(int, input().split())
D = int(input())

if D >= 3600:
    A += D // 3600
    D -= 3600 * (D // 3600)

if D >= 60:
    B += D // 60
    D -= 60 * (D // 60)

C += D


while C >= 60:
    C -= 60
    B += 1

while B >= 60:
    B -= 60
    A += 1

while A >= 24:
    A -= 24


print(A, B, C)