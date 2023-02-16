N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans = []
for i in range(Q-P+1):
  row = []
  for j in range(S-R+1):
    gi = P+i
    gj = R+j
    # print(gi, gj)
    if gi-A == gj-B:
      row.append("#")
    elif gi-A == B-gj:
      row.append("#")
    else:
      row.append(".")
  ans.append(row)

for i in range(Q-P+1):
  print("".join(ans[i]))