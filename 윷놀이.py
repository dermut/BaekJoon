result = []

for i in range(3):
    tmp = list(map(int, input().split()))
    tmp_0, tmp_1 = tmp.count(0), tmp.count(1)
    if tmp_0 == 0 and tmp_1 == 4:
        result.append('E')
    elif tmp_0 == 4 and tmp_1 == 0:
        result.append('D')
    elif tmp_0 == 3 and tmp_1 == 1:
        result.append('C')
    elif tmp_0 == 2 and tmp_1 == 2:
        result.append('B')
    else:
        result.append('A')

for i in result:
    print(i)