from collections import defaultdict
N = int(input())
kijun = [0]+list(map(int, input().split()))

Q = int(input())
queries = []
for i in range(Q):
  inp = list(map(int, input().split()))
  queries.append(inp)

state = False
dic = defaultdict(int)
for i in range(Q):
  q = queries[i]

  if q[0] == 1:
    kijun = q[1]
    state = True
    dic = defaultdict(int)
  
  if q[0] == 2:
    i = q[1]
    x = q[2]
    dic[i] += x

  if q[0] == 3:
    i = q[1]
    if state:
      print(kijun+dic[i])
    else:
      print(kijun[i]+dic[i])