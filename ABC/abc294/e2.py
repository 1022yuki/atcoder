L, N1, N2 = map(int, input().split())

right1 = 0
V1 = []
R1 = [0]
for i in range(N1):
  v, l = map(int, input().split())
  right1 += l
  R1.append(right1)
  V1.append(v)

right2 = 0
V2 = []
R2 = [0]
for i in range(N2):
  v, l = map(int, input().split())
  right2 += l
  R2.append(right2)
  V2.append(v)

# print(R1)
# print(R2)
# print(V1)
# print(V2)

i1 = 0
i2 = 0
cnt = 0
# print(i1, i2)
while i1!=N1 and i2!=N2:
  # print(i1, i2)
  v1 = V1[i1]
  v2 = V2[i2]
  left1 = R1[i1]
  left2 = R2[i2]
  right1 = R1[i1+1]
  right2 = R2[i2+1]

  # print(v1)
  # print(v2)
  # print(left1, right1)
  # print(left2, right2)
  if v1==v2:
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
  
  # print("cnt:", cnt)

  if R1[i1+1]<=R2[i2+1]:
    i1+=1
  else:
    i2+=1

print(cnt)