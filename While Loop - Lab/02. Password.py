name = input()
pwd = input()
p = input()
while p != pwd:
    p = input()
else:
    print(f"Welcome {name}!")