from itertools import combinations

N, M = map(int, input().split())

M_li = []
for i in range(1, M+1):
  M_li.append(i)

print(list(combinations(M_li, N)))

for i in list(combinations(M_li, N)):
  print(*i)