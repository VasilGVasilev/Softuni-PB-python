import math

form = input()
if form == 'square':
    a = float(input())
    res = a * a
    print(res)
elif form == 'rectangle':
    a = float(input())
    b = float(input())
    res = a * b
    print(res)
elif form == 'circle':
    r = float(input())
    res = r * r * math.pi
    print(res)
elif form == 'triangle':
    a = float(input())
    b = float(input())
    res = a * b / 2
    print(res)