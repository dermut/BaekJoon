wonsub_score = int(input())
saehee_score = int(input())
sangguen_score = int(input())
soonge_score = int(input())
gangsoo_score = int(input())

score = [wonsub_score, saehee_score, sangguen_score, soonge_score, gangsoo_score]

average_score = 0

for i in range(5):
    if score[i] < 40:
        score[i] = 40

    average_score += score[i]

average_score /= 5

print(int(average_score))