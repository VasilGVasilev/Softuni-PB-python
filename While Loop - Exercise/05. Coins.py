sum = float(input())
s = int(sum * 100)

counter = 0


while s >= 200:
    s -= 200
    counter += 1

while s >= 100:
    s -= 100
    counter += 1

while s >= 50:
    s -= 50
    counter += 1

while s >= 20:
    s -= 20
    counter += 1

while s >= 10:
    s -= 10
    counter += 1

while s >= 5:
    s -= 5
    counter += 1

while s >= 2:
    s -= 2
    counter += 1

while s >= 1:
    s -= 1
    counter += 1

print(counter)
