N, K = map(int, input().split())

cnt = 0

for red in range(1, N+1):
  for blue in range(1, N+1):
    white = K - red - blue
    if white >= 1 and white <= N:
      cnt += 1

print(cnt)