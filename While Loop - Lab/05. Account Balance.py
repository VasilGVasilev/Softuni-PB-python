p = input()

sum = 0

while p != "NoMoreMoney":

    s = float(p)
    if s < 0:
        print("Invalid operation!")
        print(f"Total: {sum:.2f}")
        break
    print(f"Increase: {s:.2f}")
    sum += s
    p = input()

else:
    print(f"Total: {sum:.2f}")