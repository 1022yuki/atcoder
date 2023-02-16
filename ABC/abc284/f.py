N = int(input())
T = list(input())

mod = 998244353

def s_n_tran(st_li, leng):
  num_li = []
  for i in range(leng):
    num_li.append(ord(st_li[i])-ord("a")+1)
  return num_li

def hash_val(num_li, leng):
  val = 0
  for i in range(leng):
    val = (val*100+num_li[i])%mod
  return val

cond = []
for i in range(N+1):
  s_fr = T[:i]
  s_ed = T[N+i:]
  s_ct = s_fr+s_ed
  s_ct.reverse()
  # print(i)
  # print(s_fr)
  # print(s_ct)
  # print(s_ed)
  # print()
  cond.append(s_fr+s_ct+s_ed)

print(T)
print(cond)

t_tran = s_n_tran(T, 2*N)
t_hash = hash_val(t_tran, 2*N)

for i in range(N+1):
  cond_tran = s_n_tran(cond[i], 2*N)
  cond_hash = hash_val(cond_tran, 2*N)
  if t_hash == cond_hash:
    ans = cond[i][:i]+cond[i][N+i:]
    print("".join(ans))
    print(i)
    exit()

print(-1)