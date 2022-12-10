N = int(input())
A = []
for i in range(N):
  a = int(input())
  A.append(a)

s_a_li = list(set(A))
s_a_li.sort()

# print(s_a_li)

B = [None]*N
# for i in range(N):
#   num = A[i]
#   for j in range(len(s_a_li)):
#     if s_a_li[j] == num:
#       B[i] = j

for i in range(N):
  num = A[i]
  left = -1
  right = len(s_a_li)
  while abs(left-right)>1:
    mid = (left+right)//2
    if s_a_li[mid] <= num:
      left = mid
    else:
      right = mid
  B[i] = left

for i in range(N):
  print(B[i])