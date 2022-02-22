goal = 10000
step = input()

if step == "Going home":
    steps = int(input())
    ss = goal - steps
    if ss > 0:
        print(f"{ss} more steps to reach goal.")
    elif ss <= 0:
        m = abs(ss)
        print("Goal reached! Good job!")
        print(f"{m} steps over the goal!")
else:
    steps = int(step)
    ss = goal - steps

    while ss > 0:
        steps = input()
        if steps == "Going home":
            step = int(input())
            ss -= step
            if ss > 0:
                print(f"{ss} more steps to reach goal.")
                break
            elif ss <= 0:
                m = abs(ss)
                print("Goal reached! Good job!")
                print(f"{m} steps over the goal!")
                break
        else:
            step = int(steps)
            ss -= step
    else:
        m = abs(ss)
        print("Goal reached! Good job!")
        print(f"{m} steps over the goal!")