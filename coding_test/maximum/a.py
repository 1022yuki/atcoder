N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
dic = defaultdict(int)

for a in A:
    dic[a] += 1

ans = 0
for k, v in dic.items():
    if v>=2:
        ans += v*(v-1)//2

print(ans)