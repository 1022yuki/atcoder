N, Q = map(int, input().split())
A = list(map(int, input().split()))

sum = [0]
for i in range(N):
  sum.append(sum[-1]+A[i])

L = []
R = []
for j in range(Q):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

for q in range(Q):
  ans = sum[R[q]] - sum[L[q]-1]
  print(ans)