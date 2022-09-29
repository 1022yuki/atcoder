a, b, c = map(int, input().split())

# sum = 0


sum = (a*(a+1)*b*(b+1)*c*(c+1)) // 8

# for a in range(1, A+1):
#   for b in range(1, B+1):
#     for c in range(1, C+1):

#       pro = a*b*c
#       sum += pro

print(sum%998244353)