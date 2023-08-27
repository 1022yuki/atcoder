N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
dic = defaultdict(int)

ans = []

for i in range(3*N):
    dic[A[i]] += 1
    if dic[A[i]] == 2:
        ans.append(A[i])

print(*ans)