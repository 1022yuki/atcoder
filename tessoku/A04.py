N = int(input())

bin_li = []

while N > 0:
  shou = N // 2
  amari = N % 2
  N = shou
  bin_li.append(str(amari))

# print(bin_li)

len = len(bin_li)

ans = '0' * (10-len)

for i in range(len-1, -1, -1):
  ans += bin_li[i]

print(ans)