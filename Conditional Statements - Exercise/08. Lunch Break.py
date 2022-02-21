import math

name = input()
episode = int(input())
rest = int(input())

lunch = rest / 8
brea = rest / 4

left = rest - (lunch + brea)

if left >= episode:
    print(f"You have enough time to watch {name} and left with {math.ceil(left - episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(abs(left-episode))} more minutes.")