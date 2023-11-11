# import sys
# sys.setrecursionlimit(10**7)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=0') 

N = int(input())
A = list(map(int, input().split()))

# dp[i][j][k]: 残りの寿司が１つの皿がi個、２つの皿がj個、３つの皿がk個の状態から、全ての皿を食べるまでの回数の期待値
dp = []
for i in range(N+1):
    dp.append([])
    for j in range(N+1):
        dp[i].append([-1]*(N+1))
dp[0][0][0] = 0

done = []
for i in range(N+1):
    done.append([])
    for j in range(N+1):
        done[i].append([False]*(N+1))
done[0][0][0] = True

def rec(i, j, k):
    if done[i][j][k]:
        return dp[i][j][k]
    done[i][j][k] = True
    res = 0
    if i > 0 and i+j+k <= N:
        res += rec(i-1, j, k) * i
    if j > 0 and i+j+k <= N:
        res += rec(i+1, j-1, k) * j
    if k > 0 and i+j+k <= N:
        res += rec(i, j+1, k-1) * k
    if i+j+k <= N:
      res += N
    dp[i][j][k] = res / (i+j+k)
    return dp[i][j][k]

ans = rec(A.count(1), A.count(2), A.count(3))

print(ans)