import math

first = int(input())
second = int(input())
third = int(input())

total = first + second + third

mins = math.floor(total // 60)
secs = total % 60

if secs < 10:
    print(f'{mins}:0{secs}')
else :
    print(f'{mins}:{secs}')