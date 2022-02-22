floor = int(input())
room = int(input())

for l in range(0, room, 1):
    print(f"L{floor}{l}", end =" ")
print()
floor -= 1
for i in range(floor, 0, -1):
    for j in range(0, room, 1):
        if i % 2 == 0:
            print(f"O{i}{j}", end = " ")
        elif i % 2 != 0:
            print(f"A{i}{j}", end = " ")
    print()