people = 0
most_people = 0

for i in range(10):
    N, M = map(int, input().split())
    people += M - N

    if people > most_people:
        most_people = people

print(most_people)