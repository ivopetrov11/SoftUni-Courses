electrons_number = int(input())
electrons_list = []
shell = 1

while electrons_number > 0:
    shell_electrons = 2 * (shell**2)
    if shell_electrons > electrons_number:
        shell_electrons = electrons_number
        electrons_list.append(shell_electrons)
        break
    else:
        electrons_number -= shell_electrons
        shell += 1

    electrons_list.append(shell_electrons)


print(electrons_list)
