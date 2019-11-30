string_base = input()
string_compare = input()

LCS = ''

for i in string_base:
    same_alphabet_index = string_compare.find(i)
    
    if same_alphabet_index == -1:
        break
    else: 
        LCS += string_compare[same_alphabet_index]
        string_compare = string_compare[same_alphabet_index:]
        if len(string_compare) == 1:
            break

    print(string_compare)
    print(LCS)

print(LCS)