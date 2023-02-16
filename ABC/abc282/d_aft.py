import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])
for i in range(M):
  u, v = map(int, input().split())
  edges[u].append(v)
  edges[v].append(u)

# print(edges)

visited = [False] * (N+1)
bin = [None] * (N+1)

cnt_0 = 0
cnt_1 = 0

def dfs(i):
  global cnt_0
  global cnt_1
  visited[i] = True
  if bin[i] == 0:
    cnt_0 += 1
  else:
    cnt_1 += 1
  for j in edges[i]:
    if visited[j]:
      if bin[i] == bin[j]:
        print(0)
        exit()
    else:
      if bin[i] == 0:
        bin[j] = 1
      else:
        bin[j] = 0
      dfs(j)
  return [cnt_0, cnt_1]
        
def check(i):
  if not visited[i]:
    bin[i] = 0
    cnt_0, cnt_1 = dfs(i)
    return [cnt_0, cnt_1]

# cnt = []
v_num = []
for i in range(1, N+1):
  bin_li = check(i)
  cnt_0 = 0
  cnt_1 = 0
  if bin_li != None:
    v_num.append(bin_li[0])
    v_num.append(bin_li[1])
# print(v_num)

# print(cnt)
# print(visited)

ans = 0
v_num_sum = sum(v_num)
for i in range(len(v_num)):
  ans += v_num[i]*(v_num_sum-v_num[i])
ans //= 2
ans -= M

print(ans)