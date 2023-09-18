N, M = map(int, input().split())

inf = 10**15
ans = inf

for a in range(1, int(M**0.5)+2):
    if a>N:
        break
    # 天井関数的な
    if M%a==0:
      b = M//a
    else:
      b = (M//a)+1
    if b>N:
        continue
    # print(a, b, a*b)
    if a*b>=M:
       ans = min(ans, a*b)

if ans==inf:
    print(-1)
else:
   print(ans)