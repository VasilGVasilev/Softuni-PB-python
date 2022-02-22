movie = input()
number = int(input())
all_tickets = 0
all_stu = 0
all_sta = 0
all_k = 0
while movie != "Finish":
    kind = 0
    student = 0
    kid = 0
    standard = 0
    tickets = 0
    perc = 0
    dividing_tickets = number
    while number != 0:
        kind = input()
        if kind == "student":
            student += 1
            number -= 1
        elif kind == "standard":
            standard += 1
            number -= 1
        elif kind == "kid":
            kid += 1
            number -= 1
        elif kind == "End":
            break
    tickets = student + standard + kid
    all_tickets += tickets
    all_stu += student
    all_sta += standard
    all_k += kid
    perc = (tickets / dividing_tickets) * 100
    print(f"{movie} - {perc:.2f}% full.")
    number = 0
    movie = input()
    if movie == "Finish":
        break
    number = int(input())
print(f"Total tickets: {all_tickets}")
s = all_stu / all_tickets * 100
print(f"{s:.2f}% student tickets.")
s = all_sta / all_tickets * 100
print(f"{s:.2f}% standard tickets.")
s = all_k / all_tickets * 100
print(f"{s:.2f}% kids tickets.")