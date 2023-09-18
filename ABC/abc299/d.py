Q = int(input())
mod = 998244353

def has_bit(n, i):
  return n & 1<<i > 0

# a の b 乗を m で割った余りを返す関数
def power(a, b, m):
  p = a
  Answer = 1
  # rangeの部分はb<2**rangeになるように調整
  for i in range(30):
    if has_bit(b, i):
      Answer = (Answer*p) % m
    p = (p * p) % m
  return Answer

qs = []
for i in range(Q):
  q = list(map(str, input().split()))
  qs.append(q)

# modを取りながら答えを管理
num = 1
# クエリ2で削除する数の桁数を管理
cnt_dig = 1
# クエリ2で削除する桁の数字を管理
from collections import deque
queue = deque()
queue.append(1)

for i in range(Q):
  q = qs[i]
  if q[0]=="1":
    x = int(q[1])
    num = (num*10+x)%mod
    cnt_dig += 1
    queue.append(x)

  if q[0]=="2":
    dig = cnt_dig
    # 削除する桁の数字
    n = queue.popleft()
    num -= (n*power(10, dig-1, mod))%mod
    cnt_dig -= 1

  if q[0]=="3":
    print(num%mod)