word = input()

word = word.lower()
word = ''.join(sorted(word))

count_alphabet = 0
longest_alphabet = 0
result = 0

while len(word) > 0:
    alphabet = word[0]
    count_alphabet = word.count(word[0])
    word = word[(word.count(word[0])):]
    if count_alphabet > longest_alphabet:
        result = alphabet.upper()
        longest_alphabet = count_alphabet
    elif count_alphabet == longest_alphabet:
        result = '?'
    else:
        pass

print(result)