import itertools

N = int(input())

group_word_count = 0

for i in range(N):
    check = input()
    check_tools = 0
    tmp_dict = { }
    check = ''.join(ch for ch, _ in itertools.groupby(check))

    for alphabet in check:
        if alphabet in tmp_dict.keys():
            check_tools = 1
            break
        else:
            tmp_dict[alphabet] = 1

    if check_tools == 1:
        pass
    else:
        group_word_count += 1   

print(group_word_count)