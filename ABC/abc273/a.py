N = int(input())

ans = [0] * 11
ans[0] = 1

for i in range(1, N+1):
  ans[i] = i*ans[i-1]

print(ans[N])