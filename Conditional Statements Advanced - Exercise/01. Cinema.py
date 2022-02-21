typ = input()
r = int(input())
c = int(input())

premier = "Premiere"
normal = "Normal"
discount = "Discount"

if typ == premier:
    print(f'{r * c * 12:.2f}')
elif typ == normal:
    print(f'{r * c * 7.5:.2f}')
elif typ == discount:
    print(f'{r * c * 5:.2f}')