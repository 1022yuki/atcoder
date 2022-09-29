import math

N, K = map(int, input().split())

A = list(map(int, input().split()))

X = []
for i in range(0, N):
  X.append(list(map(int, input().split())))

light = []
unlight = []
for i in range(0, N):
  state = True
  for have in A:
    if i == have-1:
      state = False
  if state:
    unlight.append(X[i])
  else:
    light.append(X[i])

# print(X)
# print(light)
# print(unlight)

maxd = []


for x1, y1 in unlight:
  mind = 10**10
  for x2, y2 in light:
    dist = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    mind = min(mind, dist)
  maxd.append(mind)

# print(maxd)
print(max(maxd))