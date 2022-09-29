N, M, T = map(int, input().split())
A = list(map(int, input().split()))

bonus = [0] * (N+1)
for i in range(M):
  x, y = map(int, input().split())
  bonus[x] = y


state = True

for i in range(N-1):
  T -= A[i]
  if T <= 0:
    state = False
    break
  T += bonus[i+2]

if state:
  print('Yes')
else:
  print('No')