N, M = map(int, input().split())
L = list(map(int, input().split()))

ng = 0
ok = 10**15

def check(width):
  row = 1
  cnt = 0
  top = True
  for i in range(N):
    l_word = L[i]
    if top:
      cnt += l_word
      if cnt>width:
        return False
      else:
        top = False
    else:
      cnt += 1+l_word
      if cnt>width:
        row += 1
        cnt = l_word
        if cnt>width:
          return False
      else:
        top = False
  if row <= M:
    return True
  else:
    return False

while abs(ok - ng) > 1:
  # 横幅がmidの時M行で表示できるか
  mid = (ok + ng) // 2
  if check(mid):
    ok = mid
  else:
    ng = mid

print(ok)