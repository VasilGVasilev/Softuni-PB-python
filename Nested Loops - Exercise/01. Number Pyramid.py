num = int(input())
counter = 1

for i in range(1, num + 1, 1):
    for j in range(1, i + 1, 1):
        print(counter, end=" ")
        counter += 1
        if counter > num:
            break

    print()
    if counter > num:
        break