N, M = map(int, input().split())
S = list(input())
T = list(input())

for i in range(N-M+1):
  flag = True
  for j in range(M):
    if S[i+j]!=T[j]:
      flag = False
      break
  if flag:
    for j in range(M):
      S[i+j] = "#"

# print(S)

for i in range(N-M+1):
  flag = True
  for j in range(M):
    if S[i+j]!=T[j] and S[i+j]!="#":
      flag = False
      break
  if flag:
    for j in range(M):
      S[i+j] = "#"

for i in range(N-1, -1+M-1, -1):
  flag = True
  for j in range(M-1, -1, -1):
    if S[i-j]!=T[M-1-j] and S[i-j]!="#":
      flag = False
      break
  if flag:
    for j in range(M-1, -1, -1):
      S[i-j] = "#"


# print(S)
if set(S)==set(["#"]):
  print("Yes")
else:
  print("No")