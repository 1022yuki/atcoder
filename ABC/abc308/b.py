N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

ans = 0

from collections import defaultdict
dic = defaultdict(int)

for i in range(M):
    dic[D[i]] += P[i+1]

for i in range(N):
    if dic[C[i]]==0:
        ans += P[0]
    else:
        ans += dic[C[i]]

print(ans)