from collections import defaultdict
import heapq

N, D = map(int, input().split())

day = []
for i in range(D+1):
  day.append([])
money = []

for i in range(N):
  x, y = map(int, input().split())
  day[x].append(y)

# print(day)

ans = 0
for d in range(1, D+1):
  heapq.heappush(money, 0)
  for x in day[d]:
    heapq.heappush(money, -x)
  # print(money)
  use = heapq.heappop(money)*(-1)
  ans += use

print(ans)