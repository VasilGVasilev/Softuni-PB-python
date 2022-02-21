month = input()
nights = int(input())

if month == "May" or month == "October":
    studio = 50 * nights
    apart = 65 * nights
    if nights > 14: #first the higher num of nights
        studio -= studio * 0.30
    elif nights > 7:
        studio -= studio * 0.05
elif month == "June" or month == "September":
    studio = 75.2 * nights
    apart = 68.7 * nights
    if nights > 14:
        studio -= studio * 0.20
elif month == "July" or month == "August":
    studio = 76 * nights
    apart = 77 * nights

if nights > 14:
    apart -= apart*0.1

print(f"Apartment: {apart:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")

