N, M = map(int, input().split())
A = list(map(int, input().split()))

S = []
for i in range(N):
  s = input()
  S.append(s)

NowPoints = [0] * N
for i in range(N):
  NowPoints[i] += i+1
  for j in range(M):
    if S[i][j] == 'o':
      NowPoints[i] += A[j]

# print(NowPoints)
tar = max(NowPoints)
for i in range(N):
  if NowPoints[i] == tar:
    top = i

Unsolve = []
for i in range(N):
  Unsolve.append([])
for i in range(N):
  for j in range(M):
    if S[i][j] == 'x':
      Unsolve[i].append((A[j], j))
  Unsolve[i].sort(reverse=True)

# print(Unsolve)

for i in range(N):
  if i == top:
    print(0)
    continue
  unsolve = Unsolve[i]
  now_point = NowPoints[i]
  for j in range(len(unsolve)):
    now_point += unsolve[j][0]
    if now_point > tar:
      print(j+1)
      break