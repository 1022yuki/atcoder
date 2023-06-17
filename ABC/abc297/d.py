A, B = map(int, input().split())

def culc(a, b):
  c=0
  while True:
    if a==0 or b==0:
      return c
    if a>b:
      c += a//b
      a -= (a//b)*b
    else:
      c += b//a
      b -= (b//a)*a
    if a==0 or b==0:
      return c
    if a>b:
      a-=b
    else:
      b-=a
    c += 1
  # return c

if A==B:
  print(0)
  exit()  

if A>B:
  c = A
  A = B
  B = c

cnt = 0

# dev = B//A
# cnt += dev

# B = B-(A*dev)

# if B==0:
#   print(cnt)
#   exit()

cnt += culc(A, B)

print(cnt-1)