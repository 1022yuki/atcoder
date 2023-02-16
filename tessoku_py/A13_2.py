N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
R = [None]*(N-1)
for i in range(N-1):
  if i == 0:
    R[i] = 0
  else:
    R[i] = R[i-1]
  while R[i]+1<=N-1 and A[R[i]+1]-A[i]<=K:
    R[i] += 1
  cnt += R[i]-i

print(cnt)