N, M = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict

dic = defaultdict(int)

for i in range(N):
  mod = A[i]
  dic[mod] += 1

# print(dic)
dic_s = sorted(dic.items())
# print(dic_s)

s_a = set(A)
# print(s_a)

ans_li = []
for x in s_a:
  ans = 0
  tar = x
  if dic[tar]!=0:
    ans += dic[tar]*tar
  tar = (x+1)%M
  while dic[tar] != 0:
    ans += dic[tar]*tar
    tar += 1
  tar = (x-1)%M
  while dic[tar] != 0:
    ans += dic[tar]*tar
    tar -= 1
  ans_li.append(ans)

# print(ans_li)
# print(min(ans_li))

# print(set(ans_li))
# print(sum(list(set(ans_li))))
print(sum(list(set(ans_li)))-max(list(set(ans_li))))