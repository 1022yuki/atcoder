from collections import deque

N = int(input())
S = input()
T = input()

# def has_bit(n, i):
#   return n & (i<<i) > 0

num = ['0']*N
S_q = deque()
T_q = deque()
# print(num)

for i in range(1, N+1):
  if S[i-1] == '1' and T[i-1] == '0':
    S_q.append(i)
  if S[i-1] == '0' and T[i-1] == '1':
    T_q.append(i)

# print(S_q)
# print(T_q)

while len(S_q)>0 and len(T_q)>0:
  S_q.popleft()
  T_q.popleft()

# print(S_q)
# print(T_q)

if len(S_q) == 0:
  if len(T_q)%2 == 1:
    print(-1)
    exit()
  else:
    half = len(T_q)//2
    for i in range(half):
      T_q.popleft()
    for i in range(half):
      ind = T_q.popleft()
      num[ind-1] = '1'

if len(T_q) == 0:
  if len(S_q)%2 == 1:
    print(-1)
    exit()
  else:
    half = len(S_q)//2
    for i in range(half):
      S_q.popleft()
    for i in range(half):
      ind = S_q.popleft()
      num[ind-1] = '1'

# print(num)
ans = "".join(num)
print(ans)