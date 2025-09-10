resources_dictionary = {}

while True:
    material = input()
    if material == "stop":
        break
    quantity = int(input())

    if material not in resources_dictionary.keys():
        resources_dictionary[material] = 0
    resources_dictionary[material] += quantity

# print(resources_dictionary)
for key, value in resources_dictionary.items():
    print(f"{key} -> {value}")