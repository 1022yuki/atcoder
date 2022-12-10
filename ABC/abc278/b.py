H, M = map(int, input().split())

while True:
  a = H//10
  b = H%10
  c = M//10
  d = M%10

  ac = int(str(a)+str(c))
  bd = int(str(b)+str(d))

  if 0<=ac<=23 and 0<=bd<=59:
    print(str(H)+' '+str(M))
    exit()

  M = (M+1)%60
  if M == 0:
    H = (H+1)%24

# for i in range(10):
#   M = (M+1)%60
#   if M == 0:
#     H = (H+1)%24
#   print(H, M)