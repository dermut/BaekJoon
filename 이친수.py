N = int(input())

result = 0

if N == 1:
    result += 1
    print(result)
elif N > 1 and N <= 90:
    count = '0b1' + '0' * (N - 1)
    print(count)
