X = int(input())

order = -1
accumulation_count = 0
fractional_numbers_count = 1

while X > accumulation_count:
    accumulation_count += fractional_numbers_count
    fractional_numbers_count += 1
    order *= -1

fractional_numbers_count -= 1

