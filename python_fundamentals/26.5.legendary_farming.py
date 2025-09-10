
legendary_items = {'shards' : 0, 'fragments': 0, 'motes': 0}

obtained = False

while not obtained:
    materials = input().split()

    for index in range(0, len(materials), 2):
        quantity = int(materials[index])
        item =  materials[index + 1].lower()

        if item not in legendary_items.keys():
            legendary_items[item] = 0
        legendary_items[item] += quantity

        if legendary_items['shards'] >= 250:
            legendary_items['shards'] -= 250
            print("Shadowmourne obtained!")
            obtained = True
            break

        elif legendary_items['fragments'] >= 250:
            legendary_items['fragments'] -= 250
            print("Valanyr obtained!")
            obtained = True
            break

        elif legendary_items['motes'] >= 250:
            legendary_items['motes'] -= 250
            print("Dragonwrath obtained!")
            obtained = True
            break

for key, value in legendary_items.items():
    print(f"{key}: {value}")

# materials = {"shards": 0,
#              "fragments": 0,
#              "motes": 0}
# got_legendary_item = False
# while not got_legendary_item:  # while got_legendary_item == False
#     current_items = input().split()
#     for index in range(0, len(current_items), 2):
#         value = int(current_items[index])
#         key = current_items[index + 1].lower()
#         if key not in materials.keys():
#             materials[key] = 0
#         materials[key] += value
#         if materials["shards"] >= 250:
#             materials["shards"] -= 250
#             print("Shadowmourne obtained!")
#             got_legendary_item = True
#         elif materials["fragments"] >= 250:
#             materials["fragments"] -= 250
#             print("Valanyr obtained!")
#             got_legendary_item = True
#         elif materials["motes"] >= 250:
#             materials["motes"] -= 250
#             print("Dragonwrath obtained!")
#             got_legendary_item = True
# for material, quantity in materials.items():
#     print(f"{material}: {quantity}")