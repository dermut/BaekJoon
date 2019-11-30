money = int(input())
money = 1000 - money

change = [500, 100, 50, 10, 5, 1]
number = 0

for i in change:
    while money >= i:
        number += 1
        money -= i

print(number)