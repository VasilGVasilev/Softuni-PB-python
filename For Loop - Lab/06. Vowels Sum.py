input_text = input()
x = 0
for char in input_text:
    if char == "a":
        x+=1
    elif char == "e":
        x+=2
    elif char == "i":
        x+=3
    elif char == "o":
        x+=4
    elif char == "u":
        x+=5
print(x)