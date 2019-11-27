import timeit
start = timeit.default_timer()

global count_0
global count_1
count_0, count_1 = 0, 0
memo = [0] * 50

def fibonacci(n):
    global count_0
    global count_1
    if n == 0:
        count_0 += 1
        return 0
    
    elif n == 1:
        count_1 += 1
        return 1

    elif memo[n] != 0:
        if memo[n] == 0:
            count_0 += 1
        elif memo[n] == 1:
            count_1 += 1
        return memo[n]

    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2) 
        return memo[n]


T = int(input())

result = []

for i in range(T):
    N = int(input())
    count_0, count_1 = 0, 0

    fibonacci(N)

    stop = timeit.default_timer()
    result.append([count_0, count_1])

for i in result:
    print(i[0], i[1], stop - start)