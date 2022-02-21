import math

budget = float(input())
v_card = int(input())
cpu = int(input())
ram = int(input())


v_card_sum = v_card * 250
cpu_sum = cpu * v_card_sum * 0.35
ram_sum = ram * v_card_sum * 0.1


sum = v_card_sum + cpu_sum + ram_sum

if v_card > cpu:
    total = sum - (sum*0.15)
elif v_card < cpu:
    total = sum

if budget >= total:
    print(f"You have {budget-total:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(budget-total):.2f} leva more!")