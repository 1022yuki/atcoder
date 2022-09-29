N = int(input())

S = []

for _ in range(0, N):
  si = input()
  si = list(si)
  S.append(si)

for i in range(0, N-1):
  for j in range(0, 2*N-1):
    if S[N-i-2][j]=="#":
        if S[N-i-1][j-1]=="X":
          S[N-i-2][j] = "X"
        if S[N-i-1][j]=="X":
          S[N-i-2][j] = "X"
        if S[N-i-1][j+1]=="X":
          S[N-i-2][j] = "X"

for i in range(0, N):
  S[i] = ''.join(S[i])
  print(S[i])
