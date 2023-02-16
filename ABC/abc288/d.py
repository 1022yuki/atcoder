N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
L = []
R = []
for i in range(Q):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

for i in range(Q):
  l = L[i]
  r = R[i]
  X = A[l-1:r]
  print(X)
  # print(sum(X))