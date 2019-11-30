cache = [0] * 21
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


n = int(input())
result = fibonacci(n)

print(result)