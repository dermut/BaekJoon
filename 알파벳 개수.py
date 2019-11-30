import string
S = input()

for alphabet in string.ascii_lowercase:
    print(S.count(alphabet), end=' ')