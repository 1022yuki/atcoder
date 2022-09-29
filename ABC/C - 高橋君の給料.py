import sys
sys.setrecursionlimit(1000000)

N = int(input())

# 高橋くんの社員番号は0とする
child = []
for i in range(N):
  child.append([])

for i in range(N-1):
  jousi = int(input())
  child[jousi-1].append(i+1)

print(child)


# 再帰関数
# def(i): 頂点iの子の給料を全て求め、iの給料を返す
def dfs(i):
  # 子がいないとき、1を返す
  if len(child[i]) == 0:
    return 1
  else:
    # 社員iの全ての部下の給料を求め、valuesに入れる
    values = []
    for x in child[i]:
      values.append(dfs(x))
    return max(values)+min(values)+1

print(dfs(0))