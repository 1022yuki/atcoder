from collections import deque

N = int(input())
A = list(map(int, input().split()))

A.sort()

Q = deque()

for x in A:
  Q.append(x)

# print(Q)
# print(len(Q))


ans = 0
while len(Q)>1:
  Ai = Q.pop()
  Aj = Q.popleft()
  new = Ai % Aj
  Q.appendleft(Aj)
  if new != 0:
    Q.appendleft(new)
  ans += 1
  # print(Q)

print(ans)