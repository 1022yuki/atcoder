from collections import Counter

N = int(input())

S = []
T = []

# i番目の文字列がオリジナルであるかどうか判定する配列
ORI = [True]*N

count = {}

for i in range(0, N):
  s, u = input().split()
  t = int(u)
  S.append(s)
  T.append(t)
  # if not s in count:
  #   count[s] = 0
  # if count[s] >= 1:
  #   ORI[i] = False
  # count[s] += 1

dic = Counter(S)
for i in range(N-1, -1, -1):
  if dic[S[i]] >= 2:
    ORI[i] = False
    dic[S[i]] -= 1



# for i in range(0, N):
#   for j in range(0, N):
#     if i!=j:
#       if S[i]==S[j] and i<j:
#         ORI[j] = False

high = 0
ans = 10**5

for i in range(N-1, -1, -1):
  if ORI[i] and T[i]>=high:
    ans = i+1
    high = T[i]

print(ans)