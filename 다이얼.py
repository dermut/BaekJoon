dict_dial = {'ABC': 3,
             'DEF': 4,
             'GHI': 5,
             'JKL': 6,
             'MNO': 7,
             'PQRS': 8,
             'TUV': 9,
             'WXYZ': 10}


grandmothers_dial = input()

total_time = 0

for word in grandmothers_dial:
    for i in dict_dial.keys():
        if word in i:
            total_time += dict_dial.get(i)

print(total_time)