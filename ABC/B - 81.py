N = int(input())

# if N > 81:
#   print('No')
# elif N%2==0 or N%3==0 or N%5==0 or N%7==0:
#   print('Yes')
# else:
#   print('No') 

ans = False

for i in range(1, 10):
  for j in range(1, 10):
    pro = i*j
    if pro == N:
      ans = True

if ans:
  print('Yes')
else:
  print('No')