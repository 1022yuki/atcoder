N = int(input())
S = input()
T = input()

# sがtの部分列かどうかをチェック
def check(s, t):
  # r = 0
  # lg = len(t)
  # for x in s:
  #   while r<lg and t[r]!=x:
  #     r+=1
  #   r += 1
  # # print(r)
  # if r > lg:
  #   return False
  # else:
  #   return True
  j = 0
  for i in range(len(t)):
    if j < len(s) and s[j] == t[i]:
      j+=1
  if j == len(s):
    return True
  else:
    return False

# 要素が違うので一致させることができない
if sorted(S) != sorted(T):
  print(-1)
  exit()

# 必ず一致させることができる(0~N-1回の操作)
# 操作の回数を二分探索
ng = -1
ok = N
while abs(ok-ng)>1:
  mid = (ok+ng)//2
  fix = S[mid:]
  # print(mid)
  # print(fix)
  if check(fix, T):
    ok = mid
  else:
    ng = mid

print(ok)

# print(check("aaa", "aaa"))