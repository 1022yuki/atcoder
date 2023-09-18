N, M = map(int, input().split())

visited = [False]*N
pre = [-1]*N

v = 1
while v!=N:
    inp = list(map(int, input().split()))
    edges = inp[1:]
    visited[v-1] = True
    for ni in edges:
        if not visited[ni-1]:
            print(ni, flush=True)
            pre[ni-1] = v
            v = ni
            break
    else:
      print(pre[v-1], flush=True)
      v = pre[v-1]