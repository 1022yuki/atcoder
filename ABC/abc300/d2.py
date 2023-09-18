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

for a in range(lg):
  if rekkyo[a]*rekkyo[a]*rekkyo[a]*rekkyo[a]*rekkyo[a] > N:
    break
  for b in range(a+1, lg):
    if rekkyo[a]*rekkyo[a]*rekkyo[b]*rekkyo[b]*rekkyo[b] > N:
      break
    for c in range(b+1, lg):
      if rekkyo[a]*rekkyo[a]*rekkyo[b]*rekkyo[c]*rekkyo[c] <= N:
        cnt += 1
      else:
        break

print(cnt)