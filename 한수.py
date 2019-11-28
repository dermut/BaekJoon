def one_number(n):
    tmp = str(n)
    
    if int(tmp[0]) - int(tmp[1]) == int(tmp[1]) - int(tmp[2]):
        return 1
    else:
        return 0


result = 0

N = int(input())

if N < 100:
    result = N

else:
    if N == 1000:
        N -= 1

    for i in range(100, N + 1):
        result += one_number(i)

    result += 99

print(result)