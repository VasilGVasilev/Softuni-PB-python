n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(0, n):
    l = int(input())
    if l < 200:
        p1+=1
    elif 200 <= l < 400:
        p2+=1
    elif 400 <= l < 600:
        p3+=1
    elif 600 <= l < 800:
        p4+=1
    elif l >= 800:
        p5+=1
p1 = p1 / n * 100
p2 = p2 / n * 100
p3 = p3 / n * 100
p4 = p4 / n * 100
p5 = p5 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")