from _collections import defaultdict

companies = defaultdict(list)

while True:
    line = input()
    if line == "End":
        break
    tokens = line.split(" -> ")
    name = tokens[0]
    emp_id = tokens[1]
    if emp_id not in companies[name]:
        companies[name].append(emp_id)

companies = sorted(companies.items(), key=lambda x: x[0])

for company in companies:
    print(company[0])
    for employee_id in company[1]:
        print(f"-- {employee_id}")
