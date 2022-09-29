N, K = map(int, input().split())

# 長さN
A = list(map(int, input().split()))

B = list(map(int, input().split()))

# 食べる可能性のあるおいしさ
eat = max(A)

ans = False

for i in range(0, K):
  if A[B[i]-1] == eat:
    ans = True

if ans:
  print('Yes')
else:
  print('No')