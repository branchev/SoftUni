def get_grades(grades):
    grades = [f"{g:.2f}" for g in grades]
    return ' '.join(grades)


def get_average_grade(grades):
    grades = [float(g) for g in grades]
    average = sum(grades) / len(grades)
    return f"{average:.2f}"


def printing_function(student_name_and_grades):
    for name, grades in student_name_and_grades.items():
        average_grade = get_average_grade(grades)
        grades_list = get_grades(grades)
        print(f"{name} -> {grades_list} (avg: {average_grade})")


def students_results(n):
    from collections import  defaultdict
    student_name_and_grades = defaultdict(list)
    for _ in range(n):
        name, grade = input().split(' ')
        student_name_and_grades[name].append(float(grade))
    printing_function(student_name_and_grades)


n = int(input())
students_results(n)
