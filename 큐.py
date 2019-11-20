N = int(input())

queue = []
result = []

for i in range(N):
    operation = input()

    ## push X: 정수 X를 큐에 넣는 연산이다.
    if 'push' in operation:
        operation, number = operation.split()
        number = int(number)
        queue.append(number)


    ## pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'pop':
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
            del queue[0]
            

    ## size: 큐에 들어있는 정수의 개수를 출력한다.
    elif operation == 'size':
        result.append(len(queue))


    ## empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    elif operation == 'empty':
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)


    ## front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'front':
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])

    ## back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'back':
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[len(queue) - 1])


for i in result:
    print(i)