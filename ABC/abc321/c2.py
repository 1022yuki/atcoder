# bit全探索を使って解く

K = int(input())

like_num_list = []

def has_bit(n, i):
  return (n & (1<<i) > 0)

# 数の集合を表す整数nを用意
for n in range(2, 1<<10):
  set_temp = set()
  # nのiビット目が立っているかどうかを判定
  for i in range(10):
    if has_bit(n, i):
      set_temp.add(i)
  list_temp = list(set_temp)
  list_temp.sort(reverse=True)
  num_str = ''.join(map(str, list_temp))
  like_num_list.append(int(num_str))

like_num_list.sort()
print(like_num_list[K-1])