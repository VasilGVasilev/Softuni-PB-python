name = input()
clas = 1
sum = 0

while clas != 13:
    n = float(input())
    if n < 4:
        n = float(input())
        if n < 4:
            print(f"{name} has been excluded at {clas} grade")
            break
        elif n >= 4:
            # if name does update above 4 you still need to indude the assessment as
            # part of the whole sum and for the respective grade
            sum += n
            clas += 1
    elif n >= 4:
        sum += n
        clas += 1
else:
    av = sum / 12
    print(f"{name} graduated. Average grade: {av:.2f}")
