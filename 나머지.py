numbers = [0] * 10

for i in range(10):
    numbers[i] = int(input()) % 42

numbers.sort()

length_of_numbers = len(numbers)
count_same_number = 0

while length_of_numbers > 0:
    tmp = numbers.count(numbers[0])
    length_of_numbers -= tmp
    count_same_number += 1
    for i in range(tmp):
        numbers.remove(numbers[0])

print(count_same_number)