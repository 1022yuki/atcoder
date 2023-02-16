N, K = map(int, input().split())
A = list(map(int, input().split()))

# n周するとリンゴを何個食べるかを返す
def cnt(n):
  ret = 0
  for i in range(N):
    if n <= A[i]:
      ret += n
    else:
      ret += A[i]
  return ret

# 何周するか二分探索
# left周する
left = -1
right = (10**12)+1
while abs(right-left)>1:
  mid = (left+right)//2
  if cnt(mid) <= K:
    left = mid
  else:
    right = mid

ans = A.copy()

for i in range(N):
  if ans[i] >= left:
    ans[i] -= left
  else:
    ans[i] = 0

# print(K-cnt(left))

# 端数の処理
rem = K-cnt(left)
i = 0
ct = 0
while ct < rem:
  # if i>=N:
  #   break
  if ans[i]==0:
    i+=1
  else:
    ans[i]-=1
    i+=1
    ct+=1

# for i in range(K-cnt(left)):
#   ans[i] -= 1

print(*ans)