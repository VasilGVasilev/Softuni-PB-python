N1 = int(input())
N2 = int(input())
symb = input()

if symb == "+":
    sum = N1 + N2
    if sum % 2 == 0:
        kind = "even"
    else:
        kind = "odd"
    print(f"{N1} {symb} {N2} = {sum} - {kind}")
elif symb == "-":
    sum = N1 - N2
    if abs(sum) % 2 == 0:
        kind = "even"
    else:
        kind = "odd"
    print(f"{N1} {symb} {N2} = {sum} - {kind}")

elif symb == "*":
    sum = N1 * N2
    if sum % 2 == 0:
        kind = "even"
    else:
        kind = "odd"
    print(f"{N1} {symb} {N2} = {sum} - {kind}")

elif N2 == 0:
    print(f"Cannot divide {N1} by zero")

elif symb == "/":
    sum = N1 / N2
    print(f"{N1} {symb} {N2} = {sum:.2f}")

elif symb == "%":
    sum = N1 % N2
    print(f"{N1} % {N2} = {sum}")
