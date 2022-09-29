a, b = map(int, input().split())

# scope = min(len(C[0]), len(C[1]))
# print(scope)

ans = True

# for i in range(0, scope):
#   if len(str(int(C[0][i])+int(C[1][i]))) == 2:
#     ans = False
#     print(str(int(C[0][i])+int(C[1][i])))
#     break

while a>0 and b>0:
  if a%10+b%10 >= 10:
    ans = False
    break
  a//=10
  b//=10
  
if ans:
  print('Easy')
else:
  print('Hard')