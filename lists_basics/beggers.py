donations = input().split(", ")
donations = [int(d) for d in donations]

beggars = int(input())
beggars_bank = [0 for b in range(beggars)]

beager_index = 0

for chip in donations:
    beggars_bank[beager_index] += chip
    beager_index += 1
    if  beager_index > beggars-1:
        beager_index = 0

print(beggars_bank)