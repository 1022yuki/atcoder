N = int(input())

S = []
for i in range(N):
  inp = input()
  S.append(inp)

for i in range(N):
  for j in range(N):
    if i==j:
      continue
    s1 = S[i]
    s2 = S[j]
    s3 = s1+s2
    # print(s3)
    # 回文かどうか判定
    flag = True
    for k in range(len(s3)):
      if s3[k] != s3[-k-1]:
        flag = False
        break
    if flag:
      print('Yes')
      exit()

print('No')
