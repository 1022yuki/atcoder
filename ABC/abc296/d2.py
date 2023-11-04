N, M = map(int, input().split())

# for a in range(1, N+1):
#   for b in range(1, N+1):
#     if a*b>=M:
#       print(a*b, a, b)
#       exit()

# print(-1)

INF = 10**15
ans = INF
for a in range(1, (10**6)+1):
  if M%a==0:
    b=M//a
  else:
    b=(M//a)+1
  if a<=N and b<=N:
    ans = min(ans, a*b)

if ans==INF:
  print(-1)
else:
  print(ans)