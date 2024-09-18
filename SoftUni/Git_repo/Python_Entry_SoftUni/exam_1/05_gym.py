num_of_members = int(input())
activities = ["Back", "Chest", "Legs", "Abs", "Protein shake", "Protein bar"]
back = 0
chest = 0
legs = 0
abs = 0
prot_shake = 0
prot_bar = 0
for gum_member in range(1, num_of_members + 1):
    activity_doing = input()
    if activity_doing == "Back":
        back += 1
    elif activity_doing == "Chest":
        chest += 1
    elif activity_doing == "Legs":
        legs += 1
    elif activity_doing == "Abs":
        abs += 1
    elif activity_doing == "Protein shake":
        prot_shake += 1
    elif activity_doing == "Protein bar":
        prot_bar += 1

training = ((back + chest + legs + abs)/num_of_members) * 100
protein = ((prot_bar + prot_shake)/num_of_members) * 100
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{prot_shake} - protein shake")
print(f"{prot_bar} - protein bar")
print( f"{training:.2f}% - work out")
print(f"{protein:.2f}% - protein")


