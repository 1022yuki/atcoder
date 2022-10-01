N, M, K = map(int, input().split())

road = []
cost = []
for i in range(M):
  a, b, c = map(int, input().split())
  road.append((a, b))
  cost.append(c)

E = list(map(int, input().split()))

