import sys
sys.setrecursionlimit(10**6)

N = int(input())

count = 0

def dfs(i, use3, use5, use7):
  global count
  if i<=N:
    if use3 and use5 and use7:
      count += 1
    # 末尾に3を追加
    dfs(10*i+3, True, use5, use7)

    # 末尾に5を追加
    dfs(10*i+5, use3, True, use7)

    # 末尾に7を追加
    dfs(10*i+7, use3, use5, True)

dfs(0, False, False, False)

print(count)