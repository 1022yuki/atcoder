N = int(input())
A = list(map(int, input().split()))
D = int(input())

L = []
R = []
for i in range(D):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

# 左からi部屋までのmax
l_max = [0]
# 右からi部屋までのmax
r_max = [0]

for i in range(N):
  l_max.append(max(l_max[-1], A[i]))
  r_max.append(max(r_max[-1], A[N-i-1]))

# print(l_max)
# print(r_max)

for i in range(D):
  l_data = l_max[L[i]-1]
  r_data = r_max[N-R[i]]
  print(max(l_data, r_data))