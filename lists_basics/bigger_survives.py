n_list = input().split()
count_of_removes = int(input())

list_of_numbers = list(map(int, n_list))

for _ in range(count_of_removes):
    list_of_numbers.remove(min(list_of_numbers))

print(list_of_numbers)