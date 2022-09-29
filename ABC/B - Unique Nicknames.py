N = int(input())

S = []
T = []
for i in range(0, N):
  s, t = input().split()
  S.append(s)
  T.append(t)

ans = True

for i in range(0, N):
  for j in range(0, N):
    if i != j:
      if S[i] == S[j] or S[i] == T[j]:
        for k in range(0, N):
          if i != k:
            if T[i] == T[k] or T[i] == S[k]:
              ans = False

if ans:
  print('Yes')
else:
  print('No')