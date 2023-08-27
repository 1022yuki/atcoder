N = int(input())
A = list(map(int, input().split()))

edges = []
for i in range(N):
    edges.append([])

for i in range(N):
    edges[i].append(A[i]-1)

# print(edges)

import sys
sys.setrecursionlimit(10**9)

# from collections import deque

visited = [False] * N
visited_dist = [-1] * N
# print(visited_dist)

def dfs(v, lg):
    visited_dist[v] = lg
    visited[v] = True
    lg+=1
    for next_v in edges[v]:
        if visited_dist[next_v]>=0:
            # vi_li.append(next_v)
            # print(visited_dist)
            # print(vi_li)
            # print(next_v)
            ans = []
            for i in range(len(vi_li)):
                if vi_li[i] == next_v:
                    ans = vi_li[i:]
                    break
            print(len(ans))
            for i in range(len(ans)):
                print(ans[i]+1, end=' ')
            print()    
            exit()
            
        if visited_dist[next_v]==-1:
            vi_li.append(next_v)
            dfs(next_v, lg)
            vi_li.pop()

for i in range(N):
    vi_li = []
    if not visited[i]:
        visited_dist = [-1] * N
        vi_li.append(i)
        dfs(i, 0)