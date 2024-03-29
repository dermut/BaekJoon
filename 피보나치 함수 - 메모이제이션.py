cache = [0] * 100
cache[0] = 0
cache[1] = 1

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif cache[n] != 0:
        return cache[n]
    else:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]


T = int(input())

result = []

for i in range(T):
    N = int(input())

    fibonacci(N)
    
    if N == 0:
        result.append([1, 0])
    else:
        result.append([cache[N-1], cache[N]])

for i in result:
    print(i[0], i[1])