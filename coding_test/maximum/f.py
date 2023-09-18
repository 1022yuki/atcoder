N, M, K, S = map(int, input().split())

from collections import deque
ans_li_1 = deque()
ans_li_2 = deque()

if K==S:
  if N==0:
    ans_li = ['1']*M
    print('Yes')
    print("".join(ans_li))
    exit()
  else:
    print('No')
    exit()

# ans_li_1 = []
num_0 = N
num_1 = M
while True:
    if num_0==0 and num_1==0:
      break
    if num_0>K-S:
      for n in range(K-S):
        ans_li_1.append('0')
      num_0 -= K-S
    else:
      for n in range(num_0):
        ans_li_1.append('0')
      num_0 = 0
    if num_1>S:
      for n in range(S):
        ans_li_1.append('1')
      num_1 -= S
    else:
      for n in range(num_1):
        ans_li_1.appendleft('1')
      num_1 = 0

# print(ans_li_1)
ans_li_1 = list(ans_li_1)
flag1 = True
part = ans_li_1[:K]
# print(part)
count1 = part.count('1')
if count1!=S:
  flag1 = False
for i in range((N+M)-K):
  if ans_li_1[i]=='1':
    count1 -= 1
  if ans_li_1[i+K]=='1':
    count1 += 1
  if count1!=S:
    flag1 = False

if flag1:
  print('Yes')
  print("".join(ans_li_1))
  exit()

num_0 = N
num_1 = M
while True:
    if num_0==0 and num_1==0:
      break
    if num_1>S:
      # ans_li_2.extend(['1']*S)
      for n in range(S):
        ans_li_2.append('1')
      num_1 -= S
    else:
      # ans_li_2.extend(['1']*num_1)
      for n in range(num_1):
        ans_li_2.append('1')
      num_1 = 0
    if num_0>K-S:
      # ans_li_2.extend(['0']*(K-S))
      for n in range(K-S):
        ans_li_2.append('0')
      num_0 -= K-S
    else:
      # ans_li_2.extend(['0']*num_0)
      for n in range(num_0):
        ans_li_2.appendleft('0')
      num_0 = 0

# print(ans_li_2)
ans_li_2 = list(ans_li_2)
flag2 = True
part = ans_li_2[:K]
count2 = part.count('1')
if count2!=S:
  flag2 = False
for i in range((N+M)-K):
  if ans_li_2[i]=='1':
    count2 -= 1
  if ans_li_2[i+K]=='1':
    count2 += 1
  if count2!=S:
    flag2 = False

if flag2:
  print('Yes')
  print("".join(ans_li_2))
  exit()
  
print('No')