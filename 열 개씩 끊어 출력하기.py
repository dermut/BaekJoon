N = input()

count10 = 0

for i in N:
    print(i, end='')
    count10 += 1
    if count10 == 10:
        count10 = 0
        print('')