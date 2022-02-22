n = input()
s = input()
counter = 0
is_book_found = False
while s != "No More Books":

    if s == n:
        is_book_found = True
        print(f"You checked {counter} books and found it.")
        break
    counter += 1
    s = input()
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")