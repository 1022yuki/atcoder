N = int(input())
A = []
B = []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

ans = -1
for i in range(2):
  for j in range(2):
    sum = 0
    for c in range(N):
      point = 0
      if i==0:
        point += A[c]
      else:
        point -= A[c]
      if j==0:
        point += B[c]
      else:
        point -= B[c]
      # print(point)
      if point > 0:
        sum += point
    ans = max(ans, sum)

print(ans)