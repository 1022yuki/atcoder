polyomino1 = []
polyomino2 = []
polyomino3 = []

import copy

for i in range(4):
  polyomino1.append(list(input()))
for i in range(4):
  polyomino2.append(list(input()))
for i in range(4):
  polyomino3.append(list(input()))

def shapen(polyomino):
  left = 0
  for col in range(len(polyomino[0])):
    flag = True
    for row in range(len(polyomino)):
      if polyomino[row][col] == '#':
        flag = False
    if flag:
      left = col+1
    else:
      break
  right = len(polyomino[0])
  for col in range(len(polyomino[0])-1, -1, -1):
    flag = True
    for row in range(len(polyomino)):
      if polyomino[row][col] == '#':
        flag = False
    if flag:
      right = col
    else:
      break
  top = 0
  for row in range(len(polyomino)):
    flag = True
    for col in range(len(polyomino[0])):
      if polyomino[row][col] == '#':
        flag = False
    if flag:
      top = row+1
    else:
      break
  bottom = len(polyomino)
  for row in range(len(polyomino)-1, -1, -1):
    flag = True
    for col in range(len(polyomino[0])):
      if polyomino[row][col] == '#':
        flag = False
    if flag:
      bottom = row
    else:
      break
  new_polyomino = []
  for row in range(top, bottom):
    new_polyomino.append([])
    for col in range(left, right):
      new_polyomino[row-top].append(polyomino[row][col])
  return new_polyomino
  

def rotate(polyomino):
  new_polyomino = []
  height = len(polyomino)
  width = len(polyomino[0])
  for i in range(width):
    new_polyomino.append([])
    for j in range(height):
      new_polyomino[i].append(polyomino[j][width-i-1])
  return new_polyomino


for rotate1 in range(4):
  polyomino1 = rotate(polyomino1)
  tmp_polyomino1 = shapen(polyomino1)
  for rotate2 in range(4):
    polyomino2 = rotate(polyomino2)
    tmp_polyomino2 = shapen(polyomino2)
    for rotate3 in range(4):
      polyomino3 = rotate(polyomino3)
      tmp_polyomino3 = shapen(polyomino3)
      for top_ind1 in range(4-len(tmp_polyomino1)+1):
        for left_ind1 in range(4-len(tmp_polyomino1[0])+1):
          grid_1 = []
          for n in range(4):
            grid_1.append([0]*4)
          for i1 in range(len(tmp_polyomino1)):
            for j1 in range(len(tmp_polyomino1[0])):
              if tmp_polyomino1[i1][j1] == '#':
                grid_1[top_ind1+i1][left_ind1+j1] += 1
          for top_ind2 in range(4-len(tmp_polyomino2)+1):
            for left_ind2 in range(4-len(tmp_polyomino2[0])+1):
              grid_2 = copy.deepcopy(grid_1)
              for i2 in range(len(tmp_polyomino2)):
                for j2 in range(len(tmp_polyomino2[0])):
                  if tmp_polyomino2[i2][j2] == '#':
                    grid_2[top_ind2+i2][left_ind2+j2] += 1
              for top_ind3 in range(4-len(tmp_polyomino3)+1):
                for left_ind3 in range(4-len(tmp_polyomino3[0])+1):
                  grid_3 = copy.deepcopy(grid_2)
                  for i3 in range(len(tmp_polyomino3)):
                    for j3 in range(len(tmp_polyomino3[0])):
                      if tmp_polyomino3[i3][j3] == '#':
                        grid_3[top_ind3+i3][left_ind3+j3] += 1
                  check_flg = True
                  for i in range(4):
                    for j in range(4):
                      if grid_3[i][j] != 1:
                        check_flg = False
                  if check_flg:
                    print('Yes')
                    exit()

print('No')