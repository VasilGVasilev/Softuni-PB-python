h = int(input())
m = int(input())


if m + 15 >= 60:
    m = (m + 15) % 60
    h = h + 1
elif m + 15 < 60:
    m += 15
if h == 24:
    h = 0

if m < 10:
    print(f'{h}:0{m}')
else:
    print(f'{h}:{m}')
