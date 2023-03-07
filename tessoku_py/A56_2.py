N, Q = map(int, input().split())
S = list(input())

mod = 998244353

queries = []
for i in range(Q):
  a, b, c, d = map(int, input().split())
  queries.append([a, b, c, d])

def char_num(s: str) -> int:
  return ord(s)-ord('a')+1

# hash値の基数は100
# H_pre[i]: 1文字目からi文字目までのhash値
H_pre = [0]
for i in range(N):
  H_pre.append((H_pre[-1]*100+char_num(S[i]))%mod)

# print(H_pre)

pow_100 = [1]
for i in range(N):
  pow_100.append((pow_100[-1]*100)%mod)

def hash_val(l: int, r: int) -> int:
    val = (H_pre[r]-H_pre[l-1]*pow_100[r-l+1])%mod
    return val

for i in range(Q):
  query = queries[i]
  a, b, c, d = query[0], query[1], query[2], query[3]
  # print(hash_val(a, b))
  # print(hash_val(c, d))
  if hash_val(a, b) == hash_val(c, d):
    print("Yes")
  else:
    print("No")