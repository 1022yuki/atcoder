N, Tp = map(str, input().split())
N = int(N)

S = []
for i in range(N):
  s = input()
  S.append(s)

lenTp = len(Tp)

def check(s: str, l: str):
  if len(s)>len(l):
    return check(l, s)
  if len(s)+1 < len(l):
    return False
  miss = 0
  i = 0
  j = 0
  while i<len(s) and j<len(l):
    if s[i]==l[j]:
      i += 1
      j += 1
    else:
      miss += 1
      if miss > 1:
        return False
      j += 1
      if len(s)==len(l):
        i += 1
  return True
    

ans = []
for i in range(N):
  if check(S[i], Tp):
    ans.append(i+1)

print(len(ans))
print(*ans)