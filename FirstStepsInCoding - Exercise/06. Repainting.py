protect = (int(input()) + 2) * 1.5
paint = int(input())
solution = (int(input())) * 5
hours = int(input())
all_paint = (paint + paint*10/100)*14.5
bags = 0.4
mater = protect + solution + bags + all_paint
hourly = (mater)*30/100*hours
sum = mater + hourly
print(sum)