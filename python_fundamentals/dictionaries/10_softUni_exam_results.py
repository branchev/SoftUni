from collections import defaultdict

results = defaultdict(int)
languages = defaultdict(int)

while True:
    command = input()
    if command == "exam finished":
        break
    tokens = command.split("-")
    name = tokens[0]
    if tokens[1] == "banned":
        del(results[name])
        continue
    language = tokens[1]
    languages[language] += 1
    points = int(tokens[2])
    if points > results[name] and points <= 100:
        results[name] = points

results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
languages = dict(sorted(languages.items(), key=lambda x: (-x[1], x[0])))

print("Results:")

for student, result in results.items():
    print(f"{student} | {result}")

print("Submissions:")

for lang, submissions_count in languages.items():
    print(f"{lang} - {submissions_count}")
