N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
dic = defaultdict(int)

ans = 0

for i in range(N):
  if dic[A[i]] == 1:
    ans += 1
    dic[A[i]] = 0
  else:
    dic[A[i]] = 1

print(ans)