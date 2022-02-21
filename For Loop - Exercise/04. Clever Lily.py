age = int(input())
wash = float(input())
toy = int(input())
gift_money = 0
money = 0
num_toys = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        num_toys += 1
    elif i % 2 == 0:
        gift_money += 10
        money += gift_money - 1
toy_money = num_toys * toy

if (toy_money + money) >= wash:
    n = abs((toy_money + money) - wash)
    print(f"Yes! {n:.2f}")
elif (toy_money + money) < wash:
    n = abs((toy_money + money) - wash)
    print(f"No! {n:.2f}")