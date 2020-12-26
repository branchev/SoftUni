version = list(map(int, input().split(".")))

if version[-1] != 9:
    version[-1] += 1
else:
    for index in range(len(version)-1, -1, -1):
        if version[index] != 9:
            version[index] += 1
            break
        elif version[index] == 9:
            version[index] = 0
            continue

version = list(map(str, version))
version = ".".join(version)
new_ver = ""
for i in range(len(version)):
    new_ver += version[i]
print(new_ver)
