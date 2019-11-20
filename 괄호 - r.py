T = int(input())

result_list = []

for i in range(T):
    parenthesis = input()
    
    if parenthesis[len(parenthesis)-1] == '(':
        result_list.append('NO')
    elif parenthesis.count('(') == parenthesis.count(')'):
        result_list.append('YES')
    else:
        result_list.append('NO')

for i in range(T):
    print(result_list[i])