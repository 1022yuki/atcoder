def rekkyo(n):
  ret = []
  dlt = [False] * (n+1)
  lim1 = int(n**0.5)
  for i in range(2, lim1+1):
    if dlt[i]:
      continue
    lim2 = n // i
    for j in range(2, lim2+1):
      dlt[i*j] = True

  for i in range(2, n+1):
    if not dlt[i]:
      # if i >=300:
      ret.append(i)
  
  return ret

N = int(input())

rekkyo = (rekkyo(10**6))
# print(rekkyo)

lg = len(rekkyo)
# print(lg)

cnt = 0

for a in range(1000000):
  if rekkyo[a]>=1000:
    break
  # if rekkyo[a]**5>N:
  #   break
  for b in range(a+1, 1000000):
    # r = 100
    if rekkyo[b]>=10000:
      break
    ok = b
    ng = 78498
    aab = rekkyo[a]*rekkyo[a]*rekkyo[b]
    # print(rekkyo[a], rekkyo[b])
    while abs(ng-ok)>1:
      c = (ng+ok)//2
      aabcc = aab*rekkyo[c]*rekkyo[c]
      if aabcc>N:
        ng = c
      else:
        ok = c
    cnt += ok-b
    # if rekkyo[a]**2*rekkyo[b]:
    # print(a, b)
    # for c in range(b+1, lg):
    #   # print(rekkyo[a], rekkyo[b], rekkyo[c])
    #   if rekkyo[a]*rekkyo[a]*rekkyo[b]*rekkyo[c]*rekkyo[c]<=N:
    #     cnt+=1
    #   else:
    #     continue

print(cnt)