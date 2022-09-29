from sqlite3 import Row
import numpy as np
# import pandas as pd

h1, w1 = map(int, input().split())
A = []
A_num = []
for i in range(h1):
  a = list(map(int, input().split()))
  A.append(a)
  A_num += a

h2, w2 = map(int, input().split())
B = []
B_num = []
for i in range(h2):
  b = list(map(int, input().split()))
  B.append(b)
  B_num += b

# print(A)
# print(B)
# print(A_num)
# print(B_num)

rem_row = []
rem_cul = []

for i in range(h1):
  ap = False
  for num_i in A[i]:
    for num_b in B_num:
      if num_i == num_b:
        rem_row.append(i)
        ap = True
        break
    if ap:
      break

# print(rem_row)

A2 = np.array(A).T
for i in range(w1):
  ap = False
  for num_i in A2[i]:
    for num_b in B_num:
      if num_i == num_b:
        rem_cul.append(i)
        ap = True
        break
    if ap:
      break

# print(rem_cul)

del_row = []
del_cul = []

for i in range(h1):
  # rem_rowの中にiがなかったらdel_rowに追加する
  state = True
  for x in rem_row:
    if x == i:
      state = False
  if state:
    del_row.append(i)

# print(del_row)

for i in range(w1):
  state = True
  for x in rem_cul:
    if x == i:
      state = False
  if state:
    del_cul.append(i)
  
del_row.reverse()
del_cul.reverse()

# print(del_row)
# print(del_cul)

A3 = np.array(A)

A4 = np.delete(A3, del_row, axis=0)
A5 = np.delete(A4, del_cul, axis=1)

# print(A5.shape)
row, cul = A5.shape
A6 = A5.tolist()
# print(A6)

# if A6 == B:
#   print('Yes')
# else:
#   print('No')

# print(row)
# print()

# print(row)
# print(h2)

# print(cul)
# print(w2)

# print()

if row < h2 or cul < w2:
  ans = False
else:
  ans_list = []
  for i in range(row-h2+1):
    for j in range(cul-w2+1):
      A_ans = []
      for x in A6[i:i+h2]:
        A_ans.append(x[j:j+w2])
      # print(A_ans)
      ans_list.append(A_ans)
  
  # print(ans_list)

  ans = False
  for ele in ans_list:
    if ele == B:
      ans = True
      break

if ans:
  print('Yes')
else:
  print('No')