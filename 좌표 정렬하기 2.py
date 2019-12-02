N = int(input())

array_0 = []
array_other = []

for i in range(N):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        array_0.append(tmp)
    else:
        array_other.append(tmp)


array_0.sort()
array_other.sort()
result = array_other + array_0

for i in result:
    print(i[0], i[1])