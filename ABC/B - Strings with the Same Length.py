N = int(input())
S, T = map(str, input().split())

ans = ''

for i in range(0, N):
  ans += (S[i]+T[i])

print(ans)