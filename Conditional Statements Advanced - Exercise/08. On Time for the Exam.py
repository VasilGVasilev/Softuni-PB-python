exam_h = int(input())
exam_m = int(input())
arrival_h = int(input())
arrival_m = int(input())

#exam 13:55 arrival 14:05 10  min later -> 60 - abs(5-55)
#13:50 15:00 -> 1:10 -> 60 - abs(0 - 50) = 10
#exam 14:10 arrival 14:15 5 min later -> 60 - abs(15-10) only if arrival_h == exam_h
#14:10 15:50 -> 1:40 -> 60 - abs(50 - 10)
#the 60 - abs() works only when there is a one h difference formally,
# but in reality only a few minutes due to 00-60 restart
#late arrival does work but decided on another approach
'''
if arrival_h >= exam_h:
    if arrival_h - exam_h == 0:
        sum_m = arrival_m - exam_m
        print("Late")
        print(f"{sum_m} minutes after the start")
        if sum_m < 0:
            sum_m = abs(sum_m)
            if 
    elif arrival_h - exam_h > 0:
        sum_h = arrival_h - exam_h
        sum_m = arrival_m - exam_m
        if 0 < sum_m < 10:
            print("Late")
            print(f"{sum_h}:0{sum_m} hours after the start")
        elif sum_m >= 10:
            print("Late")
            print(f"{sum_h}:{sum_m} hours after the start")
        elif sum_m < 0:
            sum_m = 60 - abs(sum_m)
            sum_h -= 1
            if 0 < sum_m < 10:
                print("Late")
                print(f"{sum_h}:0{sum_m} hours after the start")
            elif sum_m >= 10:
                print("Late")
                print(f"{sum_h}:{sum_m} hours after the start")
elif arrival_h >= exam_h:
    print("Late")
    if arrival_h - exam_h == 0:
        sum_m = arrival_m - exam_m
        print(f"{sum_m} minutes after the start")
    elif arrival_h - exam_h > 0:
        sum_h = arrival_h - exam_h
        sum_m = arrival_m - exam_m
        if 0 < sum_m < 10:
            print(f"{sum_h}:0{sum_m} hours after the start")
        elif sum_m >= 10:
            print(f"{sum_h}:{sum_m} hours after the start")
        elif sum_m < 0:
            sum_m = 60 - abs(sum_m)
            sum_h -= 1
            if 0 < sum_m < 10:
                print(f"{sum_h}:0{sum_m} hours after the start")
            elif sum_m >= 10:
                print(f"{sum_h}:{sum_m} hours after the start")


elif arrival_h == exam_h or (exam_h - arrival_h == 1 and arrival_m - exam_m):
    if arrival_m == exam_m:
        print("On time")
elif arrival_h <= exam_h:
    if arrival_m < exam_m:
        print("Early")
        if exam_h - arrival_h == 1:
            sum = 60 - arrival_m
            print(f"{sum} minutes before the start")
        elif arrival_h > exam_h:
            sum_h = arrival_h - exam_h
            sum_m = arrival_m - exam_m
            if sum_m < 10:
                print(f"{sum_h}:0{sum_m} after the start")
            print(f"{sum_h}:{sum_m} after the start")'''
#late
if arrival_m - exam_m >= 0:
    late_m = arrival_m - exam_m
    late_h = arrival_h - exam_h
    if late_h == 0:
        print(f"late {late_m} minutes after the start")
    elif late_h > 0:
        if late_m >= 10:
            print(f"late {late_h} {late_m} hours after the start")
        elif 0 <= late_m < 10:
            print(f"late {late_h} 0{late_m} hours after the start")

elif arrival_m - exam_m < 0:
    late_m = 60 - abs(arrival_m - exam_m)
    # if a mins are smaller then e mins, the a hours are always going to be bigger than e hours, otherwise
    # it will not be a late case scenario
    late_h = arrival_h - exam_h - 1
    if late_h == 0:
        print(f"late {late_m} minutes after the start")
    elif late_h > 0:
        if late_m >= 10:
            print(f"late {late_h} {late_m} hours after the start")
        elif 0 <= late_m < 10:
            print(f"late {late_h} 0{late_m} hours after the start")

#ontime
if arrival_m - exam_m == 0 and arrival_h - exam_h == 0:
    print("on time")

elif exam_m - arrival_m < 0:
    late_m = 60 - abs(exam_m - arrival_m)
    late_h = exam_h - arrival_h - 1
    if late_h == 0:
        # e 11:00 a 10:20, 20 > 00, but within an hour difference
        if late_m <= 30:
            print(f"on time {late_m} minutes before the start")
#early
        elif late_m > 30:
            print(f"early {late_m} minutes before the start")
    elif late_h > 0:
        if late_m >= 10:
            print(f"early {late_h} {late_m} hours before the start")
        elif 0 <= late_m < 10:
            print(f"early {late_h} 0{late_m} hours before the start")

elif exam_m - arrival_m >= 0:
    late_m = exam_m - arrival_m
    late_h = exam_h - arrival_h
    if late_h == 0:
        if late_m <= 30:
            print(f"on time {late_m} minutes before the start")
#early
        elif late_m > 30:
            print(f"early {late_m} minutes before the start")
    elif late_h > 0:
        if late_m >= 10:
            print(f"early {late_h} {late_m} hours before the start")
        # inlcude 0 for e 10:00 a 9:00, e < a, but 00 = 00
        elif 0 <= late_m < 10:
            print(f"early {late_h} 0{late_m} hours before the start")
