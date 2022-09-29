N = int(input())
S = input()

# for i in range(N//2):
#   if S[i] == "B":
#     state = True
#     break
#   elif S[N-i-1] == "A":
#     state = True
#     continue
#   else:
#     state = False
#     break

if N==2:
  if S == "AB" or  S == "BA":
    state = False
  else:
    state = True

if N!=2:
  if S[0] == "B" or S[-1] == "A":
    state = True
  else:
    state = False

  
if state:
  print('Yes')
else:
  print('No')