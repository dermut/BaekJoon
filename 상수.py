A, B = input().split()

inverted_A, inverted_B = A[2] + A[1] + A[0], B[2] + B[1] + B[0]

inverted_A, inverted_B = int(inverted_A), int(inverted_B)

print(inverted_A) if inverted_A > inverted_B else print(inverted_B)