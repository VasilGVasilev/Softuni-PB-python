budget = float(input())
stats = int(input())
price = float(input())
full_price = price * stats

dec = budget * 0.1

if stats > 150:
    full_price -= full_price * 0.1

sum = abs(budget - full_price - dec)

if budget >= full_price + dec:
    print("Action!")
    print(f"Wingard starts filming with {sum:.2f} leva left.")
elif budget < full_price + dec:
    print("Not enough money!")
    print(f"Wingard needs {sum:.2f} leva more.")
