N, A, B = map(int, input().split())

# Aliceが勝つための必要十分条件はn>=AかつnmodA<B
# Aliceの行動の最適は石を取れるだけ取ること

# f(X): 1<=n<=X で、nmodA<B を満たすnの個数
def f(x):
  return x//A * min(A, B) + min(x%A, B-1)

ans = f(N) - f(A-1)

# A>nのときは答えは0

print(max(ans, 0))