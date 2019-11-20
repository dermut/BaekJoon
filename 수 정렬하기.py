N = int(input())

numbers = [ ]

for i in range(N):
    numbers.append(input())

numbers = list(map(int, numbers))

numbers.sort()

for i in range(N):
    print(numbers[i])

