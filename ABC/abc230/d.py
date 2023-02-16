N, D = map(int, input().split())

W = []
for i in range(N):
  l, r = map(int, input().split())
  W.append([r, l])

W.sort()

cnt = 0
r_last = -1
for r, l in W:
  if l<=r_last:
    continue
  cnt += 1
  r_last = r+D-1

print(cnt)