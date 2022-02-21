h = int(input())
d = input()

if 10 <= h <= 18:
    if d == "Monday" or d == "Tuesday"\
            or d == "Wednesday" or d == "Thursday"\
            or d == "Friday" or d == "Saturday":
        print("open")
    elif d == "Sunday":
        print("closed")
else:
    print("closed")