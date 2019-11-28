N = input().split()
dict_N = { }

word_number = 0

for word in N:
    if dict_N.get(word) is not None:
        word_number += 1
        pass
    else:
        word_number += 1
        dict_N[word] = 1

print(word_number)