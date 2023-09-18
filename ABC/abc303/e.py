N = int(input())

ans = []
cnt = N

edges = []
for i in range(N):
    edges.append([])
for i in range(N-1):
    u, v = map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)

for i in range(N):
    li = len(edges[i])
    if li>=3:
        ans.append(li)
        cnt-=(li+1)
    # else:
    #     cnt += li

# ans.sort()
# print(ans)
# print(cnt)

ans = [2]*(cnt//3)+ans
ans.sort()
print(*ans)