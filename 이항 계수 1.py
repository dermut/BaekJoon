def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


N, K = map(int, input().split())

result = 0

if K == 0:
    result = 0
elif K > N:
    result = 0
elif K == N:
    result = 1
else:
    result = int(factorial(N) / (factorial(K) * factorial(N-K)))

print(result)