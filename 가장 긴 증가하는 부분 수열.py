N = int(input())

A = list(map(int, input().split()))

part_partial_sequence = [A[0]]
biggest_number = A[0]

for i in range(1, len(A)):
    if A[i] > biggest_number:
        biggest_number = A[i]
        part_partial_sequence.append(A[i])

print(part_partial_sequence)
print(len(part_partial_sequence))