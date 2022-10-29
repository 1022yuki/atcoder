N = int(input())

left = 1
right = 10**5

while abs(right-left) > 0.001:
  mid = (left+right) / 2
  if mid**3 + mid > N:
    right = mid
  else:
    left = mid

print(left)