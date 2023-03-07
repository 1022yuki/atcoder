from collections import defaultdict

N, M = map(int, input().split())


hikaku = []
X = set()
Y = set()
for i in range(M):
  x, y = map(int, input().split())
  hikaku.append((x, y))
  X.add(x)
  Y.add(y)


set_h = set(hikaku)
# print(set_h)

dic1 = defaultdict(list)
dic2 = defaultdict(list)

for i in range(len(set_h)):
  a, b = list(set_h)[i]
  # print(a,b)
  dic1[a].append(b)
  dic2[b].append(a)


if len(set_h)<N-1:
  print("No")
  exit()

ans = [None]*(N+1)

set = set()
for j in range(N):
  set.add(j+1)

def solve(i):

  if len(list(set-X))!=1:
    print("No")
    exit()
  if len(list(set-Y))!=1:
    print("No")
    exit()

  # print(X)
  # print(Y)

  biggest = list(set-X)[0]
  smallest = list(set-Y)[0]
  Y.remove(biggest)
  X.remove(smallest)
  # print(biggest)
  # print(smallest)
  # print(i+1)
  # print(N-i)
  ans[smallest] = i+1
  ans[biggest] = N-i
  set.remove(biggest)
  set.remove(smallest)
  for x in dic1[smallest]:
    if x in Y:
      Y.remove(x)
  for x in dic2[biggest]:
    if x in X:
      X.remove(x)


for i in range(N//2):
  solve(i)

for i in range(1, N+1):
  if ans[i] == None:
    ans[i] = (N//2)+1

print("Yes")
print(*ans[1:])