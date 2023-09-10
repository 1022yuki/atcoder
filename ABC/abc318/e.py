N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

ans = 0
dic_num = defaultdict(int)
dic_cnt = defaultdict(int)


for i in range(N):
  lg = dic_cnt[A[i]]
  if lg>0:
    # for j in dic[A[i]]:
    #   ans += i-j-1
    ans += dic_cnt[A[i]]*i - dic_num[A[i]] - dic_cnt[A[i]]
    if lg>=2:
      ans -= lg*(lg-1)//2

  dic_num[A[i]] += i
  dic_cnt[A[i]] += 1

# print(dic_num)
# print(dic_cnt)
print(ans)