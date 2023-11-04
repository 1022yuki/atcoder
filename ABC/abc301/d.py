# 10進数→2進数へ変換
def to_bin(n: int) -> int:
  ans = ''
  # nの最大値に応じて変更
  # 2**max_keta以内に収まるように
  max_keta = 60
  for i in range(max_keta, -1, -1):
    wari = n // (1<<i)
    ans += str(wari%2)
  return ans

# 2進数→10進数へ変換
# 引数は文字列型を想定
def from_bin(s: str) -> int:
  leng = len(s)
  ans = 0
  for i in range(leng):
    if s[leng-1-i] == '1':
      kurai = 1<<i
      ans += kurai
  return ans

S = input()
N = int(input())

if S.count('?') == 0:
  if from_bin(S) > N:
    print(-1)
    exit()
  else:
    print(from_bin(S))
    exit()

# liStr中の?を0,1に置き換えることでn以下にできるかどうかを判定する関数
def f(liStr: list, n: int) -> bool:
  li = liStr.copy()
  for i in range(len(li)):
    if li[i] == '?':
      li[i] = '0'
  num = from_bin(''.join(li))
  if num <= n:
    return True
  else:
    return False
  
ls = list(S)
lenS = len(S)
for i in range(lenS):
  if ls[i] == '?':
    ls[i] = '1'
    if not f(ls, N):
      ls[i] = '0'

if from_bin(''.join(ls)) > N:
  print(-1)
  exit()

print(from_bin(''.join(ls)))