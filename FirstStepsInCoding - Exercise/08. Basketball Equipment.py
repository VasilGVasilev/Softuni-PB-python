tax = int(input('Tax:'))
kec = tax - (tax/5)*2
ekip = kec - kec/5
ball = ekip/4
accessories = ball/5
sum = tax + kec + ekip + ball + accessories

print(sum)