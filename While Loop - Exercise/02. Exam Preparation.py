num = int(input())
av = 0
count = 0
bad_grade_counter = 0
name = input()
last_name = name
grade = int(input())
while name != "Enough":
    if grade <= 4:
        bad_grade_counter += 1
        av += grade
        count += 1
    elif grade > 4:
        av += grade
        count += 1
    if bad_grade_counter == num:
        print(f"You need a break, {bad_grade_counter} poor grades.")
        break
    last_name = name
    name = input()
    if name == "Enough":
        m = av / count
        print(f"Average score: {m:.2f}")
        print(f"Number of problems: {count}")
        print(f"Last problem: {last_name}")
        break
    grade = int(input())