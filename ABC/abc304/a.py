N = int(input())

S = []
A = []
for i in range(N):
  s, a = map(str, input().split())
  a = int(a)
  S.append(s)
  A.append(a)

for i in range(N):
  if A[i] == min(A):
    ind = i
    break

for i in range(ind, ind+N):
  print(S[i%N])