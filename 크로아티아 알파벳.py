croatian_list = ['c=', 'c-', 'd-','lj', 'nj', 's=']

croatian_alphabet = input()

count_alphabet = len(croatian_alphabet)

for word in croatian_list:
    count_alphabet -= croatian_alphabet.count(word)

count_alphabet -= croatian_alphabet.count('dz=') * 2
croatian_alphabet = croatian_alphabet.replace('dz=', '')
count_alphabet -= croatian_alphabet.count('z=')
    
print(count_alphabet)