import math

secs = float(input())
meters = float(input())
speed = float(input())

init_time = speed * meters

res = math.floor(meters/15)
resist = res * 12.5

sum = init_time + resist


if sum < secs:
    print(f" Yes, he succeeded! The new world record is {sum:.2f} seconds.")
elif sum >= secs:
    print(f"No, he failed! He was {abs(float(secs - sum)):.2f} seconds slower.")