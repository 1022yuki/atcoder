N, S, M, L = map(int, input().split())

max_s = (N//6)+1
max_m = (N//8)+1
max_l = (N//12)+1

ans = 10**10
for s in range(max_s+1):
  for m in range(max_m+1):
    for l in range(max_l+1):
      if 6*s+8*m+12*l >= N:
        ans = min(ans, S*s+M*m+L*l)

print(ans)