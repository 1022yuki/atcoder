N, M = map(int, input().split())

li = []
for i in range(N):
  li.append([])
for i in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  li[u].append(v)
  li[v].append(u)

# print(li)

count = 0

for n in range(N):
  # 頂点nの2つの要素j, kに注目
  for j in range(len(li[n])):
    for k in range(j+1, len(li[n])):
      for x in li[li[n][j]]:
        if x == li[n][k]:
          # print(n, j, k)
          count += 1

print(count//3)