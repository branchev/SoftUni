electrons = int(input())

shells = []
shell_number = 1

while electrons > 0:
    electrons_to_append = 2 * shell_number ** 2
    if electrons > electrons_to_append:
        shells.append(electrons_to_append)
        electrons -= electrons_to_append
    else:
        shells.append(electrons)
        electrons = 0
    shell_number += 1

print(shells)
