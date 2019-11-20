N = input().split()
dict_N = { }

for word in N:
    if dict_N.get(word) is not None:
        pass
    else:
        dict_N[word] = 1

print(len(dict_N))