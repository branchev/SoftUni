from collections import defaultdict

courses = defaultdict(list)

while True:
    command = input()
    if command == "end":
        break
    tokens = command.split(" : ")
    course_name = tokens[0]
    student = tokens[1]
    courses[course_name].append(student)

courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))

for crs_name, names_of_students in courses.items():
    print(f"{crs_name}: {len(names_of_students)}")
    names_of_students = sorted(names_of_students)
    for student in names_of_students:
        print(f"-- {student}")
