memo = input().split('-')

KMP = ''

for abbreviation in memo:
    KMP += abbreviation[0]

print(KMP)