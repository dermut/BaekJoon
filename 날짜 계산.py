E, S, M = map(int, input().split())

E_sub, S_sub, M_sub = 1, 1, 1
year = 1

while E != E_sub or S != S_sub or M != M_sub:
    E_sub += 1
    S_sub += 1
    M_sub += 1
    
    if E_sub > 15:
        E_sub -= 15
    if S_sub > 28:
        S_sub -= 28
    if M_sub > 19:
        M_sub -= 19

    year += 1

print(year)