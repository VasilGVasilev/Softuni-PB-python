holiday = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
trucks = int(input())

puzzle_p = puzzle * 2.60
doll_p = doll * 3
bear_p = bear * 4.10
minion_p = minion * 8.20
trucks_p = trucks * 2

total = puzzle + doll + bear + minion + trucks
total_p = puzzle_p + doll_p + bear_p + minion_p + trucks_p
if total >= 50:
    total_p -= total_p * 0.25

total_p -= total_p * 0.1

sum = abs(total_p - holiday)

if total_p >= holiday:
    print(f'Yes! {sum:.2f} lv left.')
else:
    print(f'Not enough money! {sum:.2f} lv needed.')