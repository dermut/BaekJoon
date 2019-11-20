N = int(input())

stack = []
result = []

for i in range(N):
    operation = input()

    ## push X: 정수 X를 스택에 넣는 연산이다.
    if 'push' in operation:
        operation, number = operation.split()
        number = int(number)
        stack.append(number)


    ## pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'pop':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])
            del stack[len(stack)-1]
            

    ## size: 스택에 들어있는 정수의 개수를 출력한다.
    elif operation == 'size':
        result.append(len(stack))


    ## empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    elif operation == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)


    ## top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])

for i in result:
    print(i)