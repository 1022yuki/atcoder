from collections import defaultdict

M = int(input())
# M*=3

s1 = list(input())
s2 = list(input())
s3 = list(input())

# dic = defaultdict(list)
# for i in range(M):
#   dic[s3[i]].append(i)

inf = 10**10
ans = inf

# for i in range(M):
#   for j in range(M):
#     if i == j:
#       continue
#     time1 = i
#     time2 = j
#     s1_tmp = s1[i]
#     s2_tmp = s2[j]
#     if s1_tmp != s2_tmp:
#       continue
#     time3 = inf
#     for k in range(len(dic[s1_tmp])):
#       time3 = min(time3, dic[s1_tmp][k])
#     if time3 != time1 and time3 != time2:
#       ans = min(ans, max(time1, time2, time3))

# print(ans) if ans != inf else print(-1)

for i in range(3*M):
  for j in range(3*M):
    for k in range(3*M):
      if i == j or j == k or k == i:
        continue
      time1 = i
      time2 = j
      time3 = k
      s1_tmp = s1[i%M]
      s2_tmp = s2[j%M]
      s3_tmp = s3[k%M]
      if s1_tmp != s2_tmp or s2_tmp != s3_tmp or s3_tmp != s1_tmp:
        continue
      ans = min(ans, max(time1, time2, time3))

print(ans) if ans != inf else print(-1)