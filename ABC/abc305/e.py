import heapq
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

# ヒープキュー
Q = []
# 確定済み頂点
done = [False]*N
# (実質の)警備員の体力
ver_keibi = [-1]*N

for i in range(K):
    p, h = map(int, input().split())
    # hが大きいものから取り出したいので、-1をかけておく
    heapq.heappush(Q, [-1*h, p-1])
    ver_keibi[p-1] = h

while True:
    if len(Q)==0:
        break
    # hが0のものが一番大きくなったら終了して良い
    if Q[0][0]==0:
        break
    
    h, n = heapq.heappop(Q)
    # -1倍していたので、元に戻す
    h *= -1

    if done[n]:
        continue
    
    for j in edges[n]:
        if ver_keibi[j] < h-1:
            heapq.heappush(Q, [-1*(h-1), j])
            ver_keibi[j] = h-1

ans = []
cnt = 0
for i in range(N):
    if ver_keibi[i] != -1:
        ans.append(i+1)
        cnt += 1

print(cnt)
print(*ans)