notes = []
sorted_notes = []
output = []

while True:
    command = input()
    if command == "End":
        print(output)
        break

    notes.append(command)

    sorted_notes = sorted(notes, key=lambda x: int(x.split("-")[0]))
    # IMPORTANT LESSON - sort() IS NOT THE SAME AS sorted()

    output = [note.split("-")[1] for note in sorted_notes]
