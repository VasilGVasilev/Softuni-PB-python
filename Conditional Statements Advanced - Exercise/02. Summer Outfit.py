deg = int(input())
day_period = input()

if 10 <= deg <= 18:
    if day_period == "Morning":
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif day_period == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif day_period == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

elif 18 < deg <= 24:
    if day_period == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif day_period == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif day_period == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

elif deg >= 25:
    if day_period == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif day_period == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
    elif day_period == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"

print(f"It's {deg} degrees, get your {Outfit} and {Shoes}.")