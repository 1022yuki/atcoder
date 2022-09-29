N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = []

for i in range(0, M):
  a.append(False)

# print(a)

for i in range(0, M):
  len = B[i]
  for j in range(0, N):
    if A[j] == len:
      A[j] = 0
      a[i] = True
      break

# print(a)
ans = True

for i in range(0, M):
  if a[i] == False:
    ans = False

if ans:
  print('Yes')
else:
  print('No')