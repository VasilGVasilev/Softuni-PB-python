l = input()
w = input()
sum = int(l) * int(w)
p = input()
while p != "STOP":
    pp = int(p)
    sum -= pp
    if sum < 0:
        print(f"No more cake left! You need {abs(sum)} pieces more.")
        #dont forget break with while loop !!!!
        break
    p = input()
else:
    print(f"{sum} pieces are left.")