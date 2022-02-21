pens = int(input()) * 5.8
markers = int(input()) * 7.2
liters = int(input()) * 1.2
discount = int(input())/100
sum = (pens + markers + liters) - ((pens + markers + liters) * discount)
print(sum)