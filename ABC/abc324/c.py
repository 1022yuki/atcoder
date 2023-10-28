import sys
def input(): return sys.stdin.readline()[:-1]

N, Tp = map(str, input().split())
N = int(N)

S = []
for i in range(N):
  s = input()
  S.append(s)

setT1 = set()
setT2 = set()
setT3 = set()
ltp = len(Tp)

# Tp[:x]とTp[x:]は最初に計算しておく
Tptox = []
Tpfromx = []
from collections import deque
top = deque()
bottom = deque(Tp)
for i in range(ltp+1):
  Tptox.append(''.join(top))
  Tpfromx.append(''.join(bottom))
  if i!=ltp:
    top.append(Tp[i])
    bottom.popleft()

# Tpから1文字削除したもの全てをsetTに追加
for i in range(ltp):
  setT1.add(''.join([Tptox[i], Tpfromx[i+1]]))

# Tpの1箇所にある英小文字1文字を追加したもの全てをsetTに追加
for i in range(ltp+1):
  for j in range(26):
    setT2.add(''.join([Tptox[i], chr(ord('a')+j), Tpfromx[i]]))

# Tpの1箇所をある英小文字1文字に変更したもの全てをsetTに追加
for i in range(ltp):
  for j in range(26):
    setT3.add(''.join([Tptox[i], chr(ord('a')+j), Tpfromx[i+1]]))

ans = []
for i in range(N):
  if abs(len(S[i])-ltp)>1:
    continue
  if len(S[i])==ltp:
    if S[i] in setT3:
      ans.append(i+1)
  if len(S[i])==ltp+1:
    if S[i] in setT2:
      ans.append(i+1)
  if len(S[i])==ltp-1:
    if S[i] in setT1:
      ans.append(i+1)

print(len(ans))
print(*ans)
