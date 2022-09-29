N = int(input())
P = list(map(int, input().split()))

Q = []

for i in range(0, N):
  Q.append(0)

# print(Q)

for i in range(0, N):
  num = P[i] -1
  # print(num)
  Q[num] = i+1

for i in range(0, N):
  print(Q[i], end=' ')