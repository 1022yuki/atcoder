H, W = map(int, input().split())

S = []
for i in range(H):
  inp = list(input())
  S.append(inp)

T = []
for j in range(H):
  inp = list(input())
  T.append(inp)

# print(S)
# print(T)

S_tate = []
T_tate = []
for i in range(W):
  S_tate.append([])
  T_tate.append([])

for i in range(H):
  for j in range(W):
    S_tate[j].append(S[i][j])
    T_tate[j].append(T[i][j])

# print()
# print(S_tate)
# print(T_tate)

S_t_n = []
T_t_n = []
for i in range(W):
  S_t_n.append([0]*H)
  T_t_n.append([0]*H)

for i in range(W):
  for j in range(H):
    if S_tate[i][j] == '#':
      S_t_n[i][j] = 1
    if T_tate[i][j] == '#':
      T_t_n[i][j] = 1

# print()
# print(S_t_n)
# print(T_t_n)

S_t_n.sort()
T_t_n.sort()

# print()
# print(S_t_n)
# print(T_t_n)

if S_t_n == T_t_n:
  print('Yes')
else:
  print('No')