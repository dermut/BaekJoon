N = int(input())

for i in range(N - 1, -1, -1):
    print(' ' * (N - (i + 1)), end='')
    print('*' * i, end='')
    print('*', end='')
    print('*' * i)