def base_10_to_x(n, x):
    res = ""
    if n == 0:
        res = "0"
    else:
        while n > 0:
            c = str(n % x)
            res = c + res
            n //= x
    return res


N, M, K, S = map(int, input().split())

for i in range(1 << (N + M)):
    cand = base_10_to_x(i, 2).zfill(N + M)
    if cand.count('1')!=M:
      continue
    flag2 = True
    part = cand[:K]
    count2 = part.count('1')
    if count2!=S:
      flag2 = False
    for i in range((N+M)-K):
      if cand[i]=='1':
        count2 -= 1
      if cand[i+K]=='1':
        count2 += 1
      if count2!=S:
        flag2 = False
    if flag2:
       print(cand)