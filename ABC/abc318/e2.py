N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
dic_l = defaultdict(int)
dic_r = defaultdict(int)

for i in range(1, N):
  dic_r[A[i]] += 1

ans = 0
diff = 0

for j in range(1, N-1):
  dic_l[A[j-1]] += 1
  dic_r[A[j+1]] -= 1 
  diff += dic_r[A[j-1]]
  diff -= dic_l[A[j+1]]
  ans += diff-dic_l[A[j]]*dic_r[A[j]]
  print(dic_l)
  print(dic_r)

print(ans)