import math

N = int(input())

X = []

for i in range(0, N):
  x = list(map(int, input().split()))
  X.append(x)

LEN = []

for i in range(0, N):
  for j in range(i+1, N):
    len = math.sqrt((X[i][0]-X[j][0])**2 + (X[i][1]-X[j][1])**2)
    LEN.append(len)

print(max(LEN))