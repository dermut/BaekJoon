def self_number(n):
    result = n
    for i in str(n):
        result += int(i)
    return result


index = [i for i in range(1, 10001)]
sub = []

for i in index:
    try:
        sub.append(self_number(i))
    except ValueError:
        pass

sub.sort()

index = [item for item in index if item not in sub]

for i in index:
    print(i)