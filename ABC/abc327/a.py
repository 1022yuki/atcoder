N = int(input())
S = input()

flag = False
for i in range(N-1):
  if S[i]=='a' and S[i+1]=='b':
    flag = True
  if S[i]=='b' and S[i+1]=='a':
    flag = True
  
if flag:
  print('Yes')
else:
  print('No')