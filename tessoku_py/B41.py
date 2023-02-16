X, Y = map(int, input().split())

def next(x, y):
  if x>y:
    x -= y
  else:
    y -= x
  return x, y

if X==1 and Y==1:
  print(0)
  exit()

ans = [[X, Y]]
nx = X
ny = Y
while True:
  x, y = ans[-1]
  nx, ny = next(x, y)
  ans.append([nx, ny])
  if nx==1 and ny==1:
    break

k = len(ans)
print(k-1)
for i in range(1, k):
  print(*ans[k-i-1])