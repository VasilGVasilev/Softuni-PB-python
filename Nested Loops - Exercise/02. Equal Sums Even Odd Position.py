num_1 = int(input())
num_2 = int(input())

for i in range(num_1, num_2 + 1):
    s = str(i)
    sum_e = 0
    sum_o = 0
    for index, digit in enumerate(s):
        if index % 2 == 0:
            sum_e += int(digit)
        elif index % 2 != 0:
            sum_o += int(digit)
        counter = 1
    if sum_o == sum_e:
        print(s, end=" ")