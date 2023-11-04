N, D, W = map(int, input().split())

T = []
X = []
timeAndLoc = []
for i in range(N):
  t, x = map(int, input().split())
  T.append(t)
  X.append(x)
  timeAndLoc.append([t, x])

timeAndLoc.sort()

# print(timeAndLoc)

TC = list(set(T))
XC = list(set(X))
TC.sort()
XC.sort()

# print(TC)
# print(XC)

from collections import defaultdict
dicT = defaultdict(int)
dicX = defaultdict(int)

for i in range(len(TC)):
  dicT[TC[i]] = i
for i in range(len(XC)):
  dicX[XC[i]] = i

# print(dicT)
# print(dicX)

# 座標圧縮&二次元累積和

# 二次元累積和
grid = []
for i in range(len(TC)):
  grid.append([0]*len(XC))

for i in range(N):
  grid[dicT[T[i]]][dicX[X[i]]] += 1

# print(grid)

sumGrid = []
for i in range(len(TC)+1):
  sumGrid.append([0]*(len(XC)+1))

# 二次元累積和
for i in range(1, len(TC)+1):
  for j in range(1, len(XC)+1):
    sumGrid[i][j] = sumGrid[i][j-1]+grid[i-1][j-1]

for j in range(1, len(XC)+1):
  for i in range(1, len(TC)+1):
    sumGrid[i][j] += sumGrid[i-1][j]

# print(sumGrid)

ans = -1

# 累積和の答え
for t in range(1, len(TC)+1):
  for x in range(1, len(XC)+1):
    # 二分探索で範囲を求める
   
    

print(ans)