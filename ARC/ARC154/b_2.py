N = int(input())
S = list(input())
T = list(input())

if sorted(S)!=sorted(T):
  print(-1)
  exit()

S.reverse()
T.reverse()

# Sの何文字目までがTの部分列になっているか
j = 0
for i in range(len(T)):
  if T[i] == S[j]:
    j += 1

print(N-j)