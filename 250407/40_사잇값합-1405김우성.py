import random as r


while True:
    start_number = list(r.choices(range(1, 10), k=2))
    start_number.sort()
    sum = 0
    for i in range(min(start_number), max(start_number) + 1):
        sum += i
    print(f'{min(start_number)} ~ {max(start_number)} => {sum}')
    if min(start_number) == max(start_number):
        break