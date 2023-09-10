N, M, P = map(int, input().split())

cnt = M
ans = 0

while cnt<=N:
  cnt += P
  ans += 1

print(ans)