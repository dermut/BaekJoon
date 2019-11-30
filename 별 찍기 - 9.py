N = int(input())

for i in range(N):
    print(' ' * i, end='')
    print('*' * (N - i - 1), end='')
    print('*', end='')
    print('*' * (N - i - 1))

for i in range(1, N):
    print(' ' * (N - i - 1), end = '')
    print('*' * i, end='')
    print('*', end='')
    print('*' * i)