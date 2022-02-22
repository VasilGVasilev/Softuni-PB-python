dest = input()
budget = float(input())

while dest != "End":
    while budget > 0:
        sum = float(input())
        budget -= sum
    print(f"Going to {dest}!")
    dest = input()
    if dest == "End":
        break
    budget = float(input())