N, M = map(int, input().split())
A = list(map(int, input().split()))

B_pre = [1]
for i in range(N-1):
  B_pre.append(i+2)
# print(B_pre)

for i in range(1, M+1):
  B = B_pre.copy()
  # print(B)
  for k in range(1, M+1):
    if k == i:
      continue
    B[A[k-1]-1], B[A[k-1]] = B[A[k-1]], B[A[k-1]-1]
  print(B)