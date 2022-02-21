length = int(input())
width = int(input())
heigth = int(input())
per = float(input())

vol = (length * width * heigth)/1000
minus = 1 - (per/100)

sum = vol * minus

print(sum)