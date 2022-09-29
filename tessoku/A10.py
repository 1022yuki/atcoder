N = int(input())
A = list(map(int, input().split()))
D = int(input())

L = []
R = []
for i in range(D):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

# 左側からの累積max
# 1-indexed
P = [0]*(N+1)
# 右側からの累積max
Q = [0]*(N+1)

P[1] = A[0]
Q[N] = A[N-1]

for i in range(2, N+1):
  P[i] = max(P[i-1], A[i-1])

for i in range(N-1, 0, -1):
  Q[i] = max(Q[i+1], A[i-1])

# print(P)
# print(Q)

for i in range(D):
  l, r = L[i], R[i]
  ans = max(P[l-1], Q[r+1])
  print(ans)