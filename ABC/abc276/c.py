import bisect

N = int(input())
P = list(map(int, input().split()))

for i in range(1, N+1):
  shojun = P[-i:]
  sort_sho = sorted(shojun)
  if sort_sho != shojun:
    break
  # print(shojun)

tar = P[-i:][0]
use_li = P[-i+1:]
ind = bisect.bisect_left(use_li, tar)-1

fir = P[-i+1:][ind]

# print(fir)
tar_li = P[-i:]
tar_li.sort()
tar_li.reverse()
tar_li.remove(fir)
# print(tar_li)

print(*(P[:-i]+[fir]+tar_li))