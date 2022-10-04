maps = ["Bind", "Accent", "Haven", "Pearl", "Ice-Box", "Fracture", "Breeze"]


for i in range(0, 3, 1):
    ban = input("Team 1, Ban: ")
    for item in maps:
        if item == ban:
            maps.remove(item)
    ban2 = input("Team 2, Ban: ")
    for item in maps:
        if item == ban2:
            maps.remove(item)
    
    new_maps = ''.join(maps)

print("Lets play,", new_maps + '!!');