N, W = map(int, input().split())

A = list(map(int, input().split()))

count = 0
J = [False]*W

for i in range(0, N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      sum = A[i] + A[j] + A[k]
      if sum <= W:
        J[sum-1] = True

for i in range(0, N):
  for j in range(i+1, N):
    sum = A[i] + A[j]
    if sum <= W:
      J[sum-1] = True

for i in range(0, N):
  sum = A[i]
  if sum <= W:
    J[sum-1] = True

for i in range(0, len(J)):
  if J[i]:
    count += 1

# print(J)
print(count)