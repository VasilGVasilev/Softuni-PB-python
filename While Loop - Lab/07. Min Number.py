p = input()
minim = 1000000

while p != "Stop":
    s = int(p)
    if s < minim:
        minim = s
    p = input()
else:
    print(minim)