num_groups = int(input())
musala = 0
monblan = 0
kili = 0
k2 = 0
everest = 0
all_people = 0
for i in range(num_groups):
    people = int(input())
    all_people += people
    if people <= 5:
        musala += people
    elif people <= 12:
        monblan += people
    elif people <= 25:
        kili += people
    elif people <= 40:
        k2 += people
    elif people > 40:
        everest += people
musala_p = musala/all_people * 100
monblan_p = monblan/all_people * 100
kili_p = kili/all_people * 100
k2_p = k2/all_people * 100
everest_p = everest/all_people * 100
print(f"{musala_p:.2f}%")
print(f"{monblan_p:.2f}%")
print(f"{kili_p:.2f}%")
print(f"{k2_p:.2f}%")
print(f"{everest_p:.2f}%")
