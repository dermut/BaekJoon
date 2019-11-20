N = input()

length_of_N = len(N) - 1

if length_of_N < 10:
    print(N[0:length_of_N])

else:
    for i in range((length_of_N // 10)+1):
        print(N[(10*i):(10*i)+10])