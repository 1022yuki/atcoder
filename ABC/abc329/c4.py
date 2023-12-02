N = int(input())
S = input()

# ランレングス圧縮
from collections import deque, defaultdict
queue = deque()
queue.append([S[0], 0])

for i in range(N):
  if queue[-1][0] == S[i]:
    queue[-1][1] += 1
  else:
    queue.append([S[i], 1])

print(queue)

dic = defaultdict(int)
for ch, num in queue:
  dic[ch] = max(dic[ch], num)

print(dic)