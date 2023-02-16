H, W = map(int, input().split())

A = []
for i in range(H):
  row = list(map(int, input().split()))
  A.append(row)

# print(A)


def is_iso(i, j):
  num = A[i][j]
  for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
    if 0<=ni<=H-1 and 0<=nj<=W-1:
      if A[ni][nj] == num:
        return False
  return True

# print(is_iso(0, 0))
def from_bin(s: str) -> int:
  leng = len(s)
  ans = 0
  for i in range(leng):
    if s[leng-1-i] == '1':
      kurai = 1<<i
      ans += kurai
  return ans

for i in range(H):
  bin = "".join(str(A[i]))
  bin = "".join(bin)
  print(bin)




iso_ind = []

for i in range(H):
  for j in range(W):
    if is_iso(i, j):
      iso_ind.append((i, j))

# print(iso_ind)

def cnt_gr(li):
  sum = 0
  for i in range(len(li)):
    for j in range(i+1, len(li)):
      dist = (li[i][0]-li[j][0]) + (li[i][1]-li[j][1])
      # print(dist)
      if abs(dist) == 1:
        sum += 1
  # print(sum)
  return len(li)-sum

print(cnt_gr(iso_ind))