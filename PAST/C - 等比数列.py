def solve(A, R, N):

  # R=1 のとき、Nの値を無視してAを返す
  if R == 1:
    return A

  # AにRをn-1回かける
  for _ in range(0, N-1):
    A *= R

    # 10**9を超えることがわかったら、途中でも終了して”large”を返す
    if A > 10**9:
      return "large"
  
  return A

A, R, N = map(int, input().split())

ans = solve(A, R, N)
print(ans)