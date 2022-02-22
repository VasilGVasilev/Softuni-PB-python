starting_number = int(input())
final_number = int(input())
num = int(input())

counter = 0
is_found = False


for i in range(starting_number, final_number + 1):
    for j in range(starting_number, final_number + 1):
        counter += 1

        if i + j == num:
            print(f'Combination N:{counter} ({i} + {j} = {num})')
            #use exit() to force exit/break
            exit()

print(f'{counter} combinations - neither equals {num}')