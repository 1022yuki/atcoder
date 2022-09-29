A, B, K = map(int, input().split())

cnt = 0

for num in range(100, 0, -1):
  if A%num==0 and B%num==0:
    cnt += 1
    if cnt == K:
      ans = num
      break

print(ans)