from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

dic = defaultdict(int)
for i in range(M):
  dic[A[i]] = 1

li = []
for i in range(1, N+1):
  li.append(i)

rot = []
l = 0
r = 1
while True:
  if r == N:
    rot.append([l, r])
    break
  if dic[r] == 1:
    r += 1
  else:
    rot.append([l, r])
    l = r
    r = l+1

for i in range(len(rot)):
  fi, la = rot[i]
  la
  rot_li = li[fi: la]
  rot_li.reverse()
  li[fi: la] = rot_li

print(*li)