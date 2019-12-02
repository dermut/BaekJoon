K = int(input())

stack = []

for i in range(K):
    tmp = int(input())
    if tmp == 0:
        del stack[len(stack)-1]
    else:
        stack.append(tmp)

print(sum(stack))