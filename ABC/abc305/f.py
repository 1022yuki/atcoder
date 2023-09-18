import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

visited = [False]*N

def dfs(n):
    if n == N:
        exit()
    inp = list(map(int, input().split()))
    edges = inp[1:]
    visited[n-1] = True
    for ni in edges:
        if not visited[ni-1]:
            print(ni, flush=True)
            dfs(ni)
            print(n, flush=True)
            inp = list(map(int, input().split()))

dfs(1)