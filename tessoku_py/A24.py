import bisect

N = int(input())
A = list(map(int, input().split()))

# dp[i]: Aのi番目までのLISの長さの最大値
dp = [None]*N

# L[i]: 長さiの部分列の最後の要素の最小値
# 答えはlen(L)
L = [-1]

for i in range(N):
  pos = bisect.bisect_left(L, A[i])
  # print(pos)
  dp[i] = pos
  if pos == len(L):
    L.append(A[i])
  else:
    L[pos] = A[i]

# print(dp)
# print(L)
# print(len(L))
print(max(dp))