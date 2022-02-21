budget = int(input())
season = input()
fisher = int(input())

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fisher <= 6: ###
    price = price - price*0.1
elif 7 <= fisher <= 11:
    price = price - price*0.15
elif fisher >= 12:
    price = price - price*0.25

if fisher % 2 == 0 and season != "Autumn":
    price = price - price*0.05

sum = budget - price

if sum >= 0:
    print(f"Yes! You have {sum:.2f} leva left.")
elif sum < 0:
    print(f"Not enough money! You need {abs(sum):.2f} leva.")