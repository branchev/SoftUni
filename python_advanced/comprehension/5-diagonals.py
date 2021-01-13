matrix = [[int(n) for n in input().split(', ')] for row in range(int(input()))]

first_diagonal = [matrix[i][i] for i in range(len(matrix[0]))]
print(f"First diagonal: {', '.join([str(n) for n in first_diagonal])}. Sum: {sum(first_diagonal)}")

row = 0
sec_diagonal = []
for j in range(len(matrix[0])-1, -1, -1):
    sec_diagonal.append(matrix[row][j])
    row += 1

print(f"Second diagonal: {', '.join([str(n) for n in sec_diagonal])}. Sum: {sum(sec_diagonal)}")