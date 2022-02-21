product = input()
city = input()
quant = float(input())

if product == "coffee":
    if city == "Sofia":
        print(quant*0.50)
    elif city == "Plovdiv":
        print(quant*0.40)
    elif city == "Varna":
        print(quant*0.45)

elif product == "water":
    if city == "Sofia":
        print(quant*0.80)
    elif city == "Plovdiv":
        print(quant*0.70)
    elif city == "Varna":
        print(quant*0.70)

elif product == "beer":
    if city == "Sofia":
        print(quant*1.20)
    elif city == "Plovdiv":
        print(quant*1.15)
    elif city == "Varna":
        print(quant*1.10)

elif product == "sweets":
    if city == "Sofia":
        print(quant*1.45)
    elif city == "Plovdiv":
        print(quant*1.30)
    elif city == "Varna":
        print(quant*1.35)

elif product == "peanuts":
    if city == "Sofia":
        print(quant*1.60)
    elif city == "Plovdiv":
        print(quant*1.50)
    elif city == "Varna":
        print(quant*1.55)