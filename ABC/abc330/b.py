N, L, R = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
  if A[i]<=L:
    print(L, end=" ")
  elif A[i]>=R:
    print(R, end=" ")
  else:
    print(A[i], end=" ")