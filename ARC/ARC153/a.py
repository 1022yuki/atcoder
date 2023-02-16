N = int(input())

gn = []

for a in range(1, 10):
  for b in range(10):
    for c in range(10):
      for d in range(10):
        for e in range(10):
          for f in range(10):
            num = e + f*10+ e*10**2 + d*10**3 + d*10**4 + c*10**5 + b*10**6 + a*10**7 + a*10**8
            gn.append(num)

gn.sort()
print(gn[N-1])