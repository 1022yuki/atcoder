from collections import defaultdict
 
N = int(input())

dic = defaultdict(int)

for a in range(1, N):
  for b in range(1, (N//a)+1):
    # print(a, b)
    dic[N-a*b] += 1

# print(dic)

cnt = 0

for c in range(1, N):
  for d in range(1, (N//c)+1):
    cnt += dic[c*d]

print(cnt)