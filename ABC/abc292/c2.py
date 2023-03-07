from collections import defaultdict
 
N = int(input())

dic = defaultdict(int)

for a in range(1, int(N**0.5)+1):
  b = N//a
  for b in range(a, b+1):
    # print(a, b)
    if a==b:
      dic[N-a*b]+=1
    else:
      dic[N-a*b]+=2

# print(dic)

cnt = 0
for c in range(1, int(N**0.5)+1):
  d = N//c
  for d in range(c, d+1):
    if c==d:
      cnt += dic[c*d]
    else:
      cnt += dic[c*d]*2

print(cnt)