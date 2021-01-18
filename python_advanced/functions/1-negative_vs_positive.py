# def print_function(positive, negative):
#     print(negative)
#     print(positive)
#     if abs(negative) > positive:
#         print("The negatives are stronger than the positives")
#     else:
#         print_function("The positives are stronger than the negatives")
#
#
# def positive_vs_negative(numbers):
#     positive = sum([x for x in numbers if x >= 0])
#     negative = sum([x for x in numbers if x < 0])
#     print_function(positive, negative)
#

line = [int(x) for x in input().split(' ')]

# positive_vs_negative(line)

negatives = sum([x for x in line if x < 0])
print(negatives)
positives = sum([x for x in line if x >= 0])
print(positives)
if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
elif positives > abs(negatives):
    print("The positives are stronger than the negatives")