N, M = map(int, input().split())

S = []
for i in range(N):
  s = list(input())
  S.append(s)

# print(S)

# for i in range(N):
#   for j in range(M):
#     if S[i][j] == 'o':
#       S[i][j] = "1"
#     else:
#       S[i][j] = "0"

# print(S)

# S2 = []

# for i in range(N):
#   li = S[i]
#   # print(S[i])
#   join = "".join(li)
#   # print(join)
#   S2.append(join)

# print(S2)

# for i in range(N):
#   for j in range(i+1, N):
#     if 
cnt = 0

for i in range(N):
  for j in range(i+1, N):
    state = True
    for m in range(M):
      if S[i][m] == "x" and S[j][m] == "x":
        state = False
    if state:
      cnt += 1

print(cnt)