S = input()

alphabet_index = [ -1 ] * 26

length_of_S = len(S)

for alphabet in S:
    if alphabet_index[ord(alphabet)-97] == -1:
        alphabet_index[ord(alphabet)-97] = S.index(alphabet)
    else:
        pass

for i in alphabet_index:
    print(i, end=' ')