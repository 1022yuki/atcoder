N = int(input())
S = list(input())

from collections import defaultdict

cnt = defaultdict(int)

nx = 0
ny = 0

cnt[(nx, ny)] += 1

for i in range(N):
  if S[i]=="R":
    nx+=1
    if cnt[(nx, ny)] >=1:
      print("Yes")
      exit()
    cnt[(nx, ny)] += 1

  if S[i]=="L":
    nx-=1
    if cnt[(nx, ny)] >=1:
      print("Yes")
      exit()
    cnt[(nx, ny)] += 1
  
  if S[i]=="U":
    ny+=1
    if cnt[(nx, ny)] >=1:
      print("Yes")
      exit()
    cnt[(nx, ny)] += 1
  
  if S[i]=="D":
    ny-=1
    if cnt[(nx, ny)] >=1:
      print("Yes")
      exit()
    cnt[(nx, ny)] += 1

# print(cnt)
print("No")