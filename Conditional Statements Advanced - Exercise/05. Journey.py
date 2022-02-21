budget = float(input())
season = input()



if budget <= 100:
    dest = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        place = "Camp"
    elif season == "winter":
        budget *= 0.7
        place = "Hotel"

elif budget <= 1000:
    dest = "Balkans"
    if season == "summer":
        budget *= 0.4
        place = "Camp"
    elif season == "winter":
        budget *= 0.8
        place = "Hotel"

elif budget > 1000:
    dest = "Europe"
    budget *= 0.9
    place = "Hotel"

print(f"Somewhere in {dest}")
print(f"{place} - {budget:.2f}")