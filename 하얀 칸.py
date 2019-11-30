result = 0

for i in range(8):
    tmp = input()

    # 검정 칸 하얀 칸
    if i % 2 == 1:
        tmp = tmp[1:: 2]
        result += tmp.count('F')
    
    # 하얀 칸 검정 칸
    elif i % 2 == 0:
        tmp = tmp[:: 2]
        result += tmp.count('F')

print(result)