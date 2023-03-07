N, Q = map(int, input().split())
S = input()

mod = 998244353

A = []
B = []
C = []
D = []
for i in range(Q):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

# 文字列Sのaを1, bを2, cを3,...に変換
T = []
for i in range(N):
  num = ord(S[i])-ord('a')+1
  T.append(num)

# print(T)

# 基数100のN乗を事前に準備
# pow100[i]: 100**i
pow100 = [1]
for i in range(N):
  pow100.append((pow100[-1]*100)%mod)

# ハッシュ値の前計算
# H[1:1], H[1:2], H[1:3],..., H[1:N] を計算
H = [0]
for i in range(N):
  H.append((H[-1]*100+T[i])%mod)

# print(H)

# l文字目からr文字目までのハッシュ値 H[l:r] を返す関数
def hash_val(l, r):
  val = (H[r] -(H[l-1]*pow100[r-l+1])) % mod
  return val

for i in range(Q):
  a, b, c, d = A[i], B[i], C[i], D[i]
  # print(hash_val(a, b))
  # print(hash_val(c, d))
  if hash_val(a, b) == hash_val(c, d):
    print('Yes')
  else:
    print('No')