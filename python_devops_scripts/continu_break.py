numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for number in numbers:
    if number == 3:
        break
    print(number)

for number in numbers:
    if number == 3:
        continue
    print(number)