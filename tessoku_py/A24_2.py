import bisect

N = int(input())
A = list(map(int, input().split()))

# dp[i]: 最後の要素がA[i]であるようなLISの長さの最大値
dp = [None]*(N+1)
dp[1] = 1
# L[x]: 長さxのLISの最後の要素のうち最小のもの
L = [-1, A[0]]

for i in range(2, N+1):
  pos = bisect.bisect_left(L, A[i-1])
  dp[i] = pos
  if pos == len(L):
    L.append(A[i-1])
  else:
    L[pos] = A[i-1]

# print(dp)
# print(L)
print(len(L)-1)