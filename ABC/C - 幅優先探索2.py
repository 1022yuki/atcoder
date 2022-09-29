from collections import deque

R, C = map(int, input().split())
si, sx = map(int, input().split())
gi, gx = map(int, input().split())

map = []
for i in range(R):
  map.append(list(input()))

print(map)

dist = []
for i in range(R):
  dist.append([-1]*C)

