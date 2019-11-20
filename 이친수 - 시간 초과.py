N = int(input())

result = 0
count = 2 ** (N - 1)

while count < (2 ** N):
    print(bin(count))
    if '0b11' in bin(count):
        break
    elif '11' in bin(count):
        # tmp는 11로 자른 부분의 앞자리
        tmp = bin(count).split('11')[0]
        tmp = int(tmp, 2) + 1
        tmp = bin(tmp)

        # tmp2는 11로 자른 부분의 뒷자리
        tmp2 = bin(count).split('11')[1]
        tmp2 += '00'

        count = int(tmp + tmp2, 2)
        pass
    else:
        result += 1
        count += 1

print(result)