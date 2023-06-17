L, N1, N2 = map(int, input().split())

from collections import defaultdict

dic = defaultdict(list)

# V1 = []
# L1 = []
right1 = 0
right2 = 0
# V2 = []
# L2 = []
for i in range(N1):
  v, l = map(int, input().split())
  # V1.append(v)
  # L1.append(l)
  left1 = right1
  right1 += l
  dic[v].append([left1, right1])

# print(dic)

cnt = 0

for i in range(N2):
  v, l = map(int, input().split())
  # V2.append(v)
  # L2.append(l)
  left2 = right2
  right2 += l
  for left1, right1 in dic[v]:
    if left1<left2 and right1>right2:
      cnt += right2-left2
    if left2<left1 and right2>right1:
      cnt += right1-left1
    if left1<=left2 and left2<=right1 and right1<=right2:
      cnt += right1-left2
    if left2<=left1 and left1<=right2 and right2<=right1:
      cnt += right2-left1

    if left1==left2 and right1==right2:
      cnt -= right1-left1
  # print(cnt)

print(cnt)