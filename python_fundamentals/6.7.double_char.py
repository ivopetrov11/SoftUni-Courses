# while True:
#     command = input()
#
#     if command == "End":
#         break
#     elif command == "SoftUni":
#         continue
#     else:
#         for i in range(len(command)):
#             print(command[i] * 2, end="" )
#         #print("\n")

command = input()

while command != "End":
    if command != "SoftUni":
        new_output = ""
        for i in range(len(command)):
            #print(command[i] * 2, end="" )
            new_output += command[i] * 2
        print(new_output)
    command = input()