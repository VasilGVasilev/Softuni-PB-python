l = int(input())
minim = 1000
maxim = -1000

for i in range(0,l):
    n = int(input())
    if n < minim:
        minim = n
    if n > maxim:
        maxim = n
print(f"Max number: {maxim}")
print(f"Min number: {minim}")