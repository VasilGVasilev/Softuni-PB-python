tabs = int(input())
salary = int(input())

for i in range(0, tabs):
    l = input()
    if l == "Facebook":
        salary -= 150
    elif l == "Instagram":
        salary -= 100
    elif l == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(salary)