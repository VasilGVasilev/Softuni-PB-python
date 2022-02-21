deposit = float(input())
period = int(input())
interest = float(input())/100
sum = period*((deposit * interest)/12) + deposit
print(sum)