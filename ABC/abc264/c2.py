h1, w1 = map(int, input().split())
A = []
for i in range(h1):
  A.append(list(map(int, input().split())))

h2, w2 = map(int, input().split())
B = []
for i in range(h2):
  B.append(list(map(int, input().split())))

R_A = 1<<h1
C_A = 1<<w1

def has_bit(n, i):
  return n&(1<<i) > 0

state = False

for n1 in range(R_A):
  row = []
  for i in range(h1):
    if has_bit(n1, i):
      row.append(i)

  for n2 in range(C_A):

    cul = []
    for j in range(w1):
      if has_bit(n2, j):
        cul.append(j)
    
    # print(row, cul)

    A_new = []
    for r in row:
      a = []
      for c in cul:
        a.append(A[r][c])
      A_new.append(a)
    # print(A_new)

    if A_new == B:
      state = True
      break

  if state:
    break

if state:
  print('Yes')
else:
  print('No')