num = int(input())
name = input()
total = 0
counter = 0
sum = 0

while name != "Finish":
    sum=0
    for i in range(0, num):
        grade = float(input())
        sum += grade
    sum /= num
    total+=sum
    counter+=1
    print(f"{name} - {sum:.2f}.")
    name = input()
else:
    total /= counter
    print(f"Student's final assessment is {total:.2f}.")