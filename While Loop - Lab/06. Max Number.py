p = input()
maxim = -100000

while p != "Stop":
    s = int(p)
    if s > maxim:
        maxim = s
    p = input()
else:
    print(maxim)