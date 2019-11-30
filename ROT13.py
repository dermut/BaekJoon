import string
# 각각 26개의 알파벳
ROT13_uppercase = string.ascii_uppercase 
ROT13_lowercase = string.ascii_lowercase

S = input()
S_ROT13 = ''

for i in S:
    index = 0
    if i.islower():
        index = ROT13_lowercase.find(i) + 13
        if index > 25:
            index -= 26

        S_ROT13 += ROT13_lowercase[index]
    elif i.isupper():
        index = ROT13_uppercase.find(i) + 13
        if index > 25:
            index -= 26
        
        S_ROT13 += ROT13_uppercase[index]
    else:
        S_ROT13 += i

print(S_ROT13)