N = int(input())

M = []
P = []
E = []

for i in range(N):
  m = int(input())
  M.append(m)
  pi = []
  ei = []
  for j in range(m):
    p, e = map(int, input().split())
    pi.append(p)
    ei.append(e)
  P.append(pi)
  E.append(ei)

print(M)
print(P)
print(E)