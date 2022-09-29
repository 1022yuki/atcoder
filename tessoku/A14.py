from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

dict = defaultdict(int)

for i in range(N):
  for j in range(N):
    sum_ab = A[i]+B[j]
    dict[sum_ab] += 1

# print(dict)

ans = 0

for i in range(N):
  for j in range(N):
    sum_cd = C[i]+D[j]
    ans += dict[K-sum_cd]

if ans >= 1:
  print('Yes')
else:
  print('No')