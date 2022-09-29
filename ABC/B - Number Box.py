N = int(input())

M = []
for i in range(0, N):
  num = list(input())
  M.append(num)


d = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

ans = 0

for i in range(0, N):
  for j in range(0, N):
      for dx, dy in d:
        cand = [M[i][j]]
        for n in range(0, N-1):
          ine, jne = (i+(n+1)*dx)%N, (j+(n+1)*dy)%N
          cand.append(M[ine][jne])
          # print(cand)
        num = 0
        for k in range(0, len(cand)):
          num += (10**(len(cand)-k-1))*int(cand[k])
        # print(num)
        ans = max(ans, num)

print(ans)