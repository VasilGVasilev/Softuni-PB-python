l = input()
w = input()
h = input()
sum = int(l) * int(w) * int(h)
p = input()
while p != "Done":
    pp = int(p)
    sum -= pp
    if sum < 0:
        print(f"No more free space! You need {abs(sum)} Cubic meters more.")
        break
    p = input()
else:
    print(f"{sum} Cubic meters left.")
