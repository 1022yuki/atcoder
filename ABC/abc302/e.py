N, Q = map(int, input().split())
qs = []
for i in range(Q):
    qs.append(list(map(int, input().split())))

edges = [set() for _ in range(N)]

ans = N

for i in range(Q):
    q = qs[i]
    if q[0]==1:
        u = q[1]-1
        v = q[2]-1
        if edges[u]==set():
                ans -= 1 
        if edges[v]==set():
                ans -= 1
        edges[u].add(v)
        edges[v].add(u)
    
    if q[0]==2:
        v = q[1]-1
        if edges[v] == set():
             ans -= 1
        li_temp = list(edges[v])
        for j in range(len(li_temp)):
            edges[li_temp[j]].discard(v)
            if edges[li_temp[j]]==set():
                ans += 1
        edges[v] = set()
        ans += 1
    # print(edges)
    print(ans)