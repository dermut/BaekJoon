verification_number = input().split()

tmp = 0

for i in verification_number:
    tmp += int(i) ** 2

print(tmp % 10)