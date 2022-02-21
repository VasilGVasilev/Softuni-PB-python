kind = input()
num = int(input())
budget = int(input())

if kind == "Roses":
    price = num * 5
    if num > 80:
        price = price - price*0.1

elif kind == "Dahlias":
    price = num * 3.8
    if num > 90:
        price = price - price*0.15

elif kind == "Tulips":
    price = num * 2.8
    if num > 80:
        price = price - price*0.15

elif kind == "Narcissus":
    price = num * 3
    if num < 120:
        price = price + price*0.15

elif kind == "Gladiolus":
    price = num * 2.5
    if num < 80:
        price = price + price*0.2

sum = budget - price

if sum >= 0:
    print(f"Hey, you have a great garden with {num} {kind} and {sum:.2f} leva left.")
elif sum < 0:
    print(f"Not enough money, you need {abs(sum):.2f} leva more.")