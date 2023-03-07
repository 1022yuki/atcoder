def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False

# 使い方
# n = 3
# a = list(range(n))
# while True:
#     print(a)
#     if not next_permutation(a, 0, n):
#         break

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  edges[a].append(b)
  edges[b].append(a)

cnt = 0

a = list(range(N))
# print(a)
# next_permutation(a, 0, N)
# print(a)
while True:
  # print(a)
  if a[0] == 0:
    flag = True
    for i in range(N-1):
      if not a[i+1] in edges[a[i]]:
        flag = False
    if flag:
      cnt += 1
  if not next_permutation(a, 0, N):
      break

print(cnt)