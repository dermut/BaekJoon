import math
X, Y = map(int, input().split())

Z = math.floor((Y / X) * 100)

upgraded_win_rate = Z + 1
game = 0



while math.floor((Y / X) * 100) >= upgraded_win_rate:
    X += 1
    Y += 1
    game += 1

print(game)