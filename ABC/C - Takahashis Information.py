C = []

for _ in range(0, 3):
  c = list(map(int, input().split()))
  C.append(c)

# a1a2 = C[0][0]-C[1][0]==C[0][1]-C[1][1]==C[0][2]-C[1][2]
# a2a3 = C[1][0]-C[2][0]==C[1][1]-C[2][1]==C[1][2]-C[2][2]
# a3a1 = C[2][0]-C[0][0]==C[2][1]-C[0][1]==C[2][2]-C[0][2]

# b1b2 = C[0][0]-C[0][1]==C[1][0]-C[1][1]==C[2][0]-C[2][1]
# b2b3 = C[0][1]-C[0][2]==C[1][1]-C[1][2]==C[2][1]-C[2][2]
# b3b1 = C[0][2]-C[0][0]==C[1][2]-C[1][0]==C[2][2]-C[2][0]

# if a1a2 and a2a3 and a3a1 and b1b2 and b2b3 and b3b1:
#   print('Yes')
# else:
#   print('No')

term1 = C[1][1]==C[1][0]+C[0][1]-C[0][0]
term2 = C[1][2]==C[1][0]+C[0][2]-C[0][0]
term3 = C[2][1]==C[2][0]+C[0][1]-C[0][0]
term4 = C[2][2]==C[2][0]+C[0][2]-C[0][0]

if term1 and term2 and term3 and term4:
  print('Yes')
else:
  print('No')