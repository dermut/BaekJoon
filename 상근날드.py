sangduck_burger = int(input())
jungduck_burger = int(input())
haduck_burger = int(input())
coke = int(input())
cider = int(input())

cheapest_burger = 0
cheapest_drink = 0

if sangduck_burger > jungduck_burger and haduck_burger > jungduck_burger:
    cheapest_burger = jungduck_burger
elif jungduck_burger > haduck_burger and sangduck_burger > haduck_burger:
    cheapest_burger = haduck_burger
else:
    cheapest_burger = sangduck_burger

if coke > cider:
    cheapest_drink = cider
else:
    cheapest_drink = coke

print(cheapest_burger + cheapest_drink - 50)