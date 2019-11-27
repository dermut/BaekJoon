T = int(input())

for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    
    n = int(input())
    planets = [[0,0,0]] * 7

    for j in range(n):
        planets[j] = list(map(int, input().split()))

    print(x1, y1, x2, y2)
    print(planets)
