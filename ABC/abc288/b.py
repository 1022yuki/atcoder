N, K = map(int, input().split())

S = []
for i in range(N):
  s = input()
  S.append(s)

li = S[:K]
li.sort()

for i in range(K):
  print(li[i])