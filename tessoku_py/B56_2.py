N, Q = map(int, input().split())
S = list(input())
S_rev = list(reversed(S))

# print(S)
# print(S_rev)

mod = 998244353

queries = []
for i in range(Q):
  l, r = map(int, input().split())
  queries.append([l, r])

def char_num(s: str) -> int:
  return ord(s)-ord('a')+1

# hash値の基数は100
# H_pre[i]: 1文字目からi文字目までのhash値
H_pre = [0]
for i in range(N):
  H_pre.append((H_pre[-1]*100+char_num(S[i]))%mod)

H_rev_pre = [0]
for i in range(N):
  H_rev_pre.append((H_rev_pre[-1]*100+char_num(S_rev[i]))%mod)

pow_100 = [1]
for i in range(N):
  pow_100.append((pow_100[-1]*100)%mod)

def hash_val(l: int, r: int, H: list) -> int:
    val = (H[r]-H[l-1]*pow_100[r-l+1])%mod
    return val

for i in range(Q):
  query = queries[i]
  l, r = query[0], query[1]
  rev_l = N-r+1
  rev_r = N-l+1
  if hash_val(l, r, H_pre) == hash_val(rev_l, rev_r, H_rev_pre):
    print("Yes")
  else:
    print("No")