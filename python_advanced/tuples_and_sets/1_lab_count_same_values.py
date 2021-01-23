def printing_template(counted_contain):
    for key, value in counted_contain.items():
        print(f"{key:.1f} - {value} times")


def value_counter(line):
    from collections import defaultdict
    result = defaultdict(int)
    for key in line.split(' '):
        result[float(key)] += 1
    printing_template(result)


value_counter(input())

