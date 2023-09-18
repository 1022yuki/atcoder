N, K = map(int, input().split())

res = [-1]*(N-K+1)

req = []
for i in range(N):
    req.append(str(i+1))

for i in range(N-K+1):
    req_i = req[i:i+K]
    req_str = '? '+' '.join(req_i)
    print(req_str, flush=True)
    t = int(input())
    res[i] = t

print(res)
ans = [-1]*N

for i in range(N-K+1):
    if res[i+1]-res[i]==0:
        ans[i+K]=0

for i in range(N-K, -1, -1):