N, Tp = map(str, input().split())
N = int(N)

S = []
for i in range(N):
  s = input()
  S.append(s)

pre = []
suf = []
for i in range(N):
  j = 0
  while j<len(Tp) and j<len(S[i]) and S[i][j]==Tp[j]:
    j += 1
  pre.append(j)
  k = 0
  while k<len(Tp) and k<len(S[i]) and S[i][len(S[i])-1-k]==Tp[len(Tp)-1-k]:
    k += 1
  suf.append(k)

# print(pre)
# print(suf)

ans = []
for i in range(N):
  if abs(len(S[i])-len(Tp))>1:
    continue
  flag = False
  # 同じ文字列
  if pre[i]==len(Tp) and suf[i]==len(Tp) and len(S[i])==len(Tp):
    flag = True
  # Tに1文字挿入してTP
  if len(S[i])+1==len(Tp) and pre[i]+suf[i]>=len(Tp)-1:
    flag = True
  # Tから1文字削除してTp
  if len(S[i])==len(Tp)+1 and pre[i]+suf[i]>=len(Tp):
    flag = True
  # Tを1文字置換してTp
  if len(S[i])==len(Tp) and pre[i]+suf[i]>=len(Tp)-1:
    flag = True
  if flag:
    ans.append(i+1)

print(len(ans))
print(*ans)