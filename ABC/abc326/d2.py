import sys
# def input(): return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**7)
import pypyjit
pypyjit.set_param('max_unroll_recursion=0') 

import copy

N = int(input())
R = list(input())
C = list(input())

# 配列aの[l, r)の部分のnext_permutation
def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    # a[l,r)の次の組み合わせ
    if r is None:
        r = len(a)
    for i in range(r - 2, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r - 1, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r - 1
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False

# 使い方
# n = 3
# a = list(range(n))
# while True:
#     print(a)
#     if not next_permutation(a, 0, n):
#         break

# N*Nのリストgridを受け取る
def check(grid):
  # グリッドの各列にa,b,cが1つずつあるか
  for j in range(N):
    cntA = 0
    cntB = 0
    cntC = 0
    for i in range(N):
      if grid[i][j]=='A':
        cntA+=1
      elif grid[i][j]=='B':
        cntB+=1
      elif grid[i][j]=='C':
        cntC+=1
    if cntA!=1 or cntB!=1 or cntC!=1:
      return False
  # グリッドのi行目に書かれた文字のうち、最も左にある文字がRのi文字目と一致するか
  mostLeftStr = []
  for i in range(N):
    for j in range(N):
      if grid[i][j]!='.':
        mostLeftStr.append(grid[i][j])
        break
  for i in range(N):
    if mostLeftStr[i]!=R[i]:
      return False
  # グリッドのi列目に書かれた文字のうち、最も上にある文字がCのi文字目と一致するか
  mostUpStr = []
  for j in range(N):
    for i in range(N):
      if grid[i][j]!='.':
        mostUpStr.append(grid[i][j])
        break
  for j in range(N):
    if mostUpStr[j]!=C[j]:
      return False
  return True

def rec(x :str, grid :list) -> bool:
    if x == 'D':
        # print(grid)
        if check(grid):
            print('Yes')
            for i in range(N):
              print(''.join(grid[i]))
            exit()
        else:
            return
    a = list(range(N))
    while True:
        tmpGrid = copy.deepcopy(grid)
        flag = True
        for i in range(N):
            if tmpGrid[i][a[i]] != '.':
                flag = False
                break
            tmpGrid[i][a[i]] = x
        if flag:
          rec(chr(ord(x)+1), tmpGrid)
        if not next_permutation(a, 0, N):
            break


flg = rec('A', [['.']*N for _ in range(N)])

if flg:
  print('Yes')
else:
  print('No')