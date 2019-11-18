a = int(input())

for i in range(a):
    print(" " * i, end='')
    b = a - i
    print("*" * b)