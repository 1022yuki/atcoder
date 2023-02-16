N = int(input())
S = []
for i in range(N):
  s = input()
  S.append(s)
for i in range(N-1, -1, -1):
  print(S[i])