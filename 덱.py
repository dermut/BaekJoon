N = int(input())

deque = []
result = []

for i in range(N):
    operation = input()

    ## push_front X: 정수 X를 덱의 앞에 넣는다.
    if 'push_front' in operation:
        operation, number = operation.split()
        number = int(number)
        deque = [number] + deque[:]

    ## push_back X: 정수 X를 덱의 뒤에 넣는다.
    elif 'push_back' in operation:
        operation, number = operation.split()
        number = int(number)
        deque.append(number)

    ## pop_front: 덱에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'pop_front':
        if len(deque) == 0:
            result.append(-1)
        else:
            result.append(deque[0])
            del deque[0]
     
    ## pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'pop_back':
        if len(deque) == 0:
            result.append(-1)
        else:
            result.append(deque[len(deque) - 1])
            del deque[len(deque) - 1]

    ## size: 덱에 들어있는 정수의 개수를 출력한다.
    elif operation == 'size':
        result.append(len(deque))


    ## empty: 덱이 비어있으면 1, 아니면 0을 출력한다.
    elif operation == 'empty':
        if len(deque) == 0:
            result.append(1)
        else:
            result.append(0)

    ## front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'front':
        if len(deque) == 0:
            result.append(-1)
        else:
            result.append(deque[0])

    ## back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    elif operation == 'back':
        if len(deque) == 0:
            result.append(-1)
        else:
            result.append(deque[len(deque) - 1])

for i in result:
    print(i)