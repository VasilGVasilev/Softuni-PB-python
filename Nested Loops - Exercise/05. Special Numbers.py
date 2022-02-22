number = int(input())
for i in range(1111, 10000):
    m = ""
    s = str(i)
    for x in s:
        if int(x) == 0:
            break
        elif number % int(x) != 0:
            break
        elif number % int(x) == 0:
            m += str(x)
    if m == s:
        print(s, end = " ")