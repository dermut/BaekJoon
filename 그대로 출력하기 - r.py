with open('new.txt', 'w') as f:
    while True:
        line = input()
        if line is not '':
            f.write(line)
        else: break

with open('new.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)