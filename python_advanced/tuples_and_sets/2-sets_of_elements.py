a = [int(x) for x in input().split(' ')]
n, m = a[0:]

set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(input())
for _ in range(m):
    set_m.add(input())

n_and_m_intersection = set_m & set_n
for item in n_and_m_intersection:
    print(item)