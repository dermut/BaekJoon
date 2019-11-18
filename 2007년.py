x, y = map(int, input().split())

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
number_of_days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if x == 1:
    print(days[y % 7])
else:
    result = 0

    for i in range(x-1):
        result += number_of_days_per_month[i]

    result += y

    print(days[result % 7])