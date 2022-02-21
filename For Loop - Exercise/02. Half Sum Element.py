n = int(input())
sum = 0
maxim = -100
for i in range(0, n):
    l = int(input())
    sum+=l
    if l > maxim:
        maxim = l
s = sum
if maxim == s / 2:
    print("Yes")
    print(f"Sum = {maxim}")
elif maxim != s / 2:
    print("No")
    print(f"Diff = {abs(maxim - (sum - maxim))}")