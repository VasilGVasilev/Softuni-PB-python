num = input()
sum_p = 0
sum_o = 0

while num != "stop":
    number = int(num)
    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    elif number < 0:
        print("Number is negative.")
    # check if flag is True
    if flag:
        sum_o += number
    else:
        # because the default is flag = False so it takes negative numbers and adds them to sum_p
        if number < 0:
            number = 0
        elif number > 1:
            sum_p += number

    num = input()
else:
    print(f"Sum of all prime numbers is: {sum_p}")
    print(f"Sum of all non prime numbers is: {sum_o}")
