l = int(input())

sum_e = 0
sum_o = 0

for i in range(0, l):
    n = int(input())
    if i % 2 != 0:
        sum_o += n
    elif i % 2 == 0:
        sum_e += n

if sum_e - sum_o == 0:
    print(f"Yes")
    print(f"Sum = {sum_e}")
elif sum_e - sum_o != 0:
    s = abs(sum_e - sum_o)
    print(f"No")
    print(f"Diff = {s}")