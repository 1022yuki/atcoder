S = list(map(int, input()))

# S.sort()

# # print(S)

# for i in range(0, 9):
#   if S[i] != i:
#     print(i)
#     break
#   elif i == 8:
#     print(9)

flag = []
for i in range(0, 10):
  flag.append(True)

# print(flag)

for i in range(0, 9):
  flag[S[i]] = False

for i in range(0, 10):
  if flag[i]:
    print(i)