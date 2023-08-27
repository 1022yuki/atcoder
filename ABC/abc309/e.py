N, M = map(int, input().split())
pts = list(map(int, input().split()))
X = []
Y = []

edges = []
for i in range(N):
    edges.append([])
for i in range(N-1):
    edges[pts[i]-1].append(i+1)

# print(edges)

for i in range(M):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ver_str = [-1]*N

import heapq
Q = []
done = [False]*N

for i in range(M):
    x, y = X[i], Y[i]
    ver_str[x-1] = y
    heapq.heappush(Q, (-y, x-1))


# print(Q)
while len(Q)>0:
    # print(Q)
    str, i = heapq.heappop(Q)

    if done[i]:
        continue
    if str == 0:
        continue
    
    done[i] = True

    str *= -1

    for j in edges[i]:
        if ver_str[j]==-1 or ver_str[j]<str-1:
            heapq.heappush(Q, (-1*(str-1), j))
            ver_str[j] = str-1

# print(ver_str)

ans = 0
for i in range(N):
    if ver_str[i] >= 0:
        ans += 1

print(ans)