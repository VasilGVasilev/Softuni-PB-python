l = int(input())
sum_1 = 0
sum_2 = 0
for i in range(0,l):
    n = int(input())
    sum_1 += n
for i in range(0,l):
    n = int(input())
    sum_2 += n
if sum_1 - sum_2 == 0:
    print(f"Yes, sum = {sum_1}")
elif sum_1 - sum_2 != 0:
    s = abs(sum_1 - sum_2)
    print(f"No, diff = {s}")