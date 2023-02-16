import math
N = int(input())

bor = int(N**0.5)
# print(bor)

ans = 0
for i in range(1, bor+1):
  ans += N//i

for i in range(1, bor+1):
  left = N//(i+1)+1
  right = N//i
  ans += i*(right-left+1)
  
print(ans)

# def check(n):
#   ng = -1
#   ok = N+1
#   while abs(ok-ng)>1:
#     mid = (ok+ng)//2
#     if mid*mid==n:
#       return mid
#     elif mid*mid<n:
#       ng = mid
#     else:
#       ok = mid
#   if ok*ok == n:
#     return ok
#   if ng*ng == n:
#     return ng
#   # print((ng, ok))
#   return False


# heiho = check(N)
# if heiho:
#   ans -= heiho

# print(ans)