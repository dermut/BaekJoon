N = int(input())

for i in range(N):
    print(' ' * (N - i - 1), end='')
    print('*' * i, end='')
    print('*', end='')
    print('*' * i)


for i in range(N - 1):
    print(' ' * (i + 1), end='')
    print('*' * (N - i - 2), end='')
    print('*', end='')
    print('*' * (N - i - 2))