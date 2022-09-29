N = int(input())
H = list(map(int, input().split()))

dif = []
for i in range(N-1):
  dif.append(H[i]-H[i+1])

# print(dif)

ans = 0

cnt = 0
for x in dif:
  if x >= 0:
    cnt += 1
  else:
    ans = max(ans, cnt)
    cnt = 0

ans = max(ans, cnt)

print(ans)