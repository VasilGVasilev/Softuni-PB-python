holiday = float(input())
budget = float(input())
counter_s = 0
days = 0

while budget < holiday:
    kind = input()
    amount = float(input())
    if kind == "spend":
        budget -= amount
        if budget < 0:
            budget = 0
        counter_s += 1
        days += 1
    elif kind == "save":
        budget += amount
        # it restarts the counter due to an instance of spending
        counter_s = 0
        days += 1
    if counter_s == 5:
        print(f"You can't save the money.")
        print(f"{days}")
        break
else:
    print(f"You saved the money for {days} days.")