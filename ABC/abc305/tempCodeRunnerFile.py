import sys
def input(): return sys.stdin.readline()[:-1]

N, M, K = map(int, input().split())

edges = []
for i in range(N):
    edges.append([])

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

import heapq
Q = []
done = [False]*N
keibi = []
ver_keibi = [-1]*N
for i in range(K):
    p, h = map(int, input().split())
    heapq.heappush(Q, [-1*h, p-1])
    keibi.append([-1*h, p-1])
    ver_keibi[p-1] = h

ans = []
cnt = 0
while True:
    if len(Q)==0:
        break
    if Q[0][0]==0:
        break
    
    h, n = heapq.heappop(Q)
    h *= -1

    if done[n]:
        continue
    
    for j in edges[n]:
        if ver_keibi[j] < h-1:
            heapq.heappush(Q, [-1*(h-1), j])
            ver_keibi[j] = h-1

for i in range(N):
    if ver_keibi[i] != -1:
        ans.append(i+1)
        cnt += 1

print(cnt)
print(*ans)