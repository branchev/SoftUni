from _collections import defaultdict

students = defaultdict(list)

n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())
    students[name].append(grade)

passed = {}

for student, grades in students.items():
    av_grade = sum(grades) / len(grades)
    if av_grade >= 4.5:
        passed[student] = av_grade

passed = sorted(passed.items(), key =lambda x: x[1], reverse=True)
for student in passed:
    print(f"{student[0]} -> {student[1]:.2f}")
