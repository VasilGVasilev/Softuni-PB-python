days = int(input()) - 1
kind = input()
review = input()

if kind == "room for one person":
    price = days * 18
    if review == "positive":
        price += price * 0.25
        print(f"{price:.2f}")
    elif review == "negative":
        price -= price * 0.1
        print(f"{price:.2f}")
elif kind == "apartment":
    price = days * 25
    if days <= 10:
        price -= price*0.3
        if review == "positive":
            price += price * 0.25
            print(f"{price:.2f}")
        elif review == "negative":
            price -= price * 0.1
            print(f"{price:.2f}")
    elif days <= 15:
        price = price - price*0.35
        if review == "positive":
            price += price * 0.25
            print(f"{price:.2f}")
        elif review == "negative":
            price -= price * 0.1
            print(f"{price:.2f}")
    elif days > 15:
        price -= price*0.5
        if review == "positive":
            price += price * 0.25
            print(f"{price:.2f}")
        elif review == "negative":
            price -= price * 0.1
            print(f"{price:.2f}")
elif kind == "president apartment":
    price = days * 35
    if days <= 10:
        price -= price*0.1
        if review == "positive":
            price += price * 0.25
            print(f"{price:.2f}")
        elif review == "negative":
            price -= price * 0.1
            print(f"{price:.2f}")
    elif days <= 15:
        price -= price*0.15
        if review == "positive":
            price += price * 0.25
            print(f"{price:.2f}")
        elif review == "negative":
            price -= price * 0.1
            print(f"{price:.2f}")
    elif days > 15:
        price -= price*0.2
        if review == "positive":
            price += price * 0.25
            print(f"{price:.2f}")
        elif review == "negative":
            price -= price * 0.1
            print(f"{price:.2f}")
