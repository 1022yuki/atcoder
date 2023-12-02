N = int(input())
S = [0]+list(input())

# S の空でない部分文字列であって、
# 1 種類の文字のみからなるものの数を求めてください
# 尺取り法

aSet = set()

cnt = 0
R = [-1]*(N+1)

for i in range(1, N+1):
  st = [S[i], 1]
  aSet.add((st[0], st[1]))
  if i==1:
    R[i] = 1
  elif S[i-1]==S[i]:
    R[i] = R[i-1]
  else:
    R[i] = i
  
  while(R[i]<N and S[R[i]+1]==S[i]):
    R[i] += 1
    st[1] += 1
    aSet.add((S[i], st[1]))

# print(R)

print(len(aSet))