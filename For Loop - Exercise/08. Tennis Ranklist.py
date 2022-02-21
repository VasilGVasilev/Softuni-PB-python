tournaments = int(input())
starting_points = int(input())
average_counter = 0
winner = 0
for i in range(tournaments):
    result = input()
    if result == "W":
        starting_points += 2000
        average_counter += 2000
        winner += 1
    elif result == "F":
        starting_points += 1200
        average_counter += 1200
    elif result == "SF":
        starting_points += 720
        average_counter += 720
average_counter /= tournaments
wins_percent = (winner / tournaments) * 100
print(f"Final points: {starting_points}")
print(f"Average points: {int(average_counter)}")
print(f"{wins_percent:.2f}%")