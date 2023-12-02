D = int(input())

ans = 10**18
for x in range(2*10**6):
  if D-x*x<0:
    continue
  ycond = int((D-x*x)**0.5)
  for y in range(ycond-10, ycond+10):
    if y>0:
      ans = min(ans, abs(x*x+y*y-D))

print(ans)