N, K = map(int, input().split())
A = list(map(int, input().split()))

big_li = []
for i in range(K):
  big_li.append([])

for i in range(N):
  big_li[i%K].append(A[i])

# print(big_li)

for k in range(K):
  big_li[k].sort()

# print(big_li)

best_sort = []

for i in range(N):
  best_sort.append(big_li[i%K][i//K])

# print(best_sort)

state = True
for i in range(N-1):
  if best_sort[i] > best_sort[i+1]:
    state = False
    break

if state:
  print('Yes')
else:
  print('No')