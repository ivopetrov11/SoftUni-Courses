phonebook_dictionary = {}

while True:
    entry = input()
    if "-" not in entry:
        for _ in range(int(entry)):
            name = input()
            if name in phonebook_dictionary.keys():
                print(f"{name} -> {phonebook_dictionary[name]}")
            else:
                print(f"Contact {name} does not exist.")
        break
    else:
        contact = entry.split("-")
        phonebook_dictionary[contact[0]] = contact[1]