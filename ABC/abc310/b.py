N, M = map(int, input().split())

P = []
C = []
F = []

for i in range(N):
    inp = list(map(int, input().split()))
    p = inp[0]
    c = inp[1]
    f = set(inp[2:])
    P.append(p)
    C.append(c)
    F.append(f)

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        si = F[i]
        sj = F[j]
        if P[i] >= P[j]:
          # siがsjの部分集合であるか判定
          if si.issubset(sj):
          # if 
              # print(si-sj)
              if P[i]>P[j] or len(sj-si)>0:
                  print('Yes')
                  # print(i, j)
                  exit()

print('No')