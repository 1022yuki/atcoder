from math import floor


N = int(input())

cnt = 0

for a in range(1, N+1):
  if a**3>N:
    break
  for b in range(a, N+1):
    if a*b*b>N:
      break
    # for c in range(b, int(N/(a*b))+1):
    #   cnt += 1
    cnt += floor(N/(a*b))-b+1

print(cnt)