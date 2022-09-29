ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())

bector_AB = [bx-ax, by-ay]
bector_BC = [cx-bx, cy-by]
bector_CD = [dx-cx, dy-cy]
bector_DA = [ax-dx, ay-dy]

# print(bector_AB)
# print(bector_BC)
# print(bector_CD)

cross1 = (bector_AB[0] * bector_DA[1] * -1) + (bector_AB[1] * bector_DA[0])
cross2 = (bector_BC[0] * bector_AB[1] * -1) + (bector_BC[1] * bector_AB[0])
cross3 = (bector_CD[0] * bector_BC[1] * -1) + (bector_CD[1] * bector_BC[0])
cross4 = (bector_DA[0] * bector_CD[1] * -1) + (bector_DA[1] * bector_CD[0])

# print(cross1)
# print(cross2)
# print(cross3)
# print(cross4)

if cross1 > 0 and cross2 > 0 and cross3 > 0 and cross4 > 0:
  print('Yes')
else:
  print('No')