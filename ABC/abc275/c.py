grid = []
for i in range(9):
  s = input()
  grid.append(s)

cnt = 0
for a in range(1,10):
  for b in range(1,10):
    for c in range(1,10):
      for d in range(1,10):
        if grid[a-1][b-1] != '#' or grid[c-1][d-1] != '#':
          continue
        if a == c and b == d:
          continue
        e1 = c-(b-d)
        f1 = d+a-c
        g1 = a-(b-d)
        h1 = a+b-c
        e2 = c+b-d
        f2 = d-(a-c)
        g2 = a+b-d
        h2 = b-(a-c)
        if 1 <= e1 <= 9 and 1 <= f1 <= 9:
          if 1 <= g1 <= 9 and 1 <= h1 <= 9:
            if grid[e1-1][f1-1] == '#' and grid[g1-1][h1-1] == '#':
              # print(a,b,c,d,e1,f1,g1,h1)
              cnt += 1
        if 1 <= e2 <= 9 and 1 <= f2 <= 9:
          if 1 <= g2 <= 9 and 1 <= h2 <= 9:
            if grid[e2-1][f2-1] == '#' and grid[g2-1][h2-1] == '#':
              # print(a,b,c,d,e2,f2,g2,h2)
              cnt += 1


print(cnt//8)