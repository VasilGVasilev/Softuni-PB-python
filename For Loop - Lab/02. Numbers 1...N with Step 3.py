n = int(input())
for i in range(1, n + 1, 3):
    print(i)
#The range() function defaults to 0 as a starting value,
#however it is possible to specify the starting value by adding
#a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
#thus n + 1