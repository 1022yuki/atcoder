N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [0] * N

# iは左側, R[i]は右側
for i in range(1, N):
  # スタート地点を決める
  if i == 1:
    R[i] = 1
  else:
    R[i] = R[i-1]
  
  # ギリギリまで増やしていく
  while R[i] < N and A[R[i]] - A[i-1] <= K:
    R[i] += 1

# print(R)

ans = 0
for i in range(1, N):
  ans += R[i] - i

print(ans)