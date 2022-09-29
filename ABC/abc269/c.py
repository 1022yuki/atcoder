N = int(input())

def has_bit(n, i):
  return n & 1<<i > 0

bin_N = bin(N)
str_bin_N = str(bin_N)

digit = len(str(bin_N)) - 2

# print(bin_N)
# print(digit)

bin_dig = []
for dig in range(digit):
  if has_bit(N, dig):
    bin_dig.append(dig)

# print(bin_dig)

all = 1<<(len(bin_dig))

for n in range(all):
  ans = 0
  for i in range(len(bin_dig)):
    if has_bit(n, i):
      ans += 1<<bin_dig[i]
  print(ans)