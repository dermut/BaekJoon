T = int(input())

P = []

for i in range(T):
    R, S = input().split()

    R = int(R)

    tmp_alphanumeric = ''
    
    for alphanumeric in S:
        tmp_alphanumeric += alphanumeric * R

    P.append(tmp_alphanumeric)

for i in range(T):
    print(P[i])