city = input()
s = float(input())

if city == "Sofia":
    if 0 <= s <= 500:
        print(f'{s*0.05:.2f}')
    elif 500 < s <= 1000:
        print(f'{s*0.07:.2f}')
    elif 1000 < s <= 10000:
        print(f'{s*0.08:.2f}')
    elif s > 10000:
        print(f'{s*0.12:.2f}')
    else:
        print("error")

elif city == "Varna":
    if 0 <= s <= 500:
        print(f'{s*0.045:.2f}')
    elif 500 < s <= 1000:
        print(f'{s*0.075:.2f}')
    elif 1000 < s <= 10000:
        print(f'{s*0.1:.2f}')
    elif s > 10000:
        print(f'{s*0.13:.2f}')
    else:
        print("error")

elif city == "Plovdiv":
    if 0 <= s <= 500:
        print(f'{s*0.055:.2f}')
    elif 500 < s <= 1000:
        print(f'{s*0.08:.2f}')
    elif 1000 < s <= 10000:
        print(f'{s*0.12:.2f}')
    elif s > 10000:
        print(f'{s*0.145:.2f}')
    else:
        print("error")
else:
    print("error")