N, M = map(int, input().split())
A = list(map(int, input().split()))

li = [0]*(N+1)

for i in range(M):
  li[A[i]] += 1

for i in range(1, N+1):
  print(M-li[i])