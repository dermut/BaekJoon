x, y, w, h = map(int, input().split())

w_len, h_len = abs(x - w), abs(y - h)

result = [x, y, w_len, h_len]
result.sort()

print(result[0])