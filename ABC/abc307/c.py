Ha, Wa = map(int, input().split())

grid_a = []
for i in range(Ha):
    inp = input()
    grid_a.append(inp)

ga_i_min = 10
ga_i_max = -1
ga_j_min = 10
ga_j_max = -1
for i in range(Ha):
    for j in range(Wa):
        if grid_a[i][j] == '#':
            if i < ga_i_min:
                ga_i_min = i
            if i > ga_i_max:
                ga_i_max = i
            if j < ga_j_min:
                ga_j_min = j
            if j > ga_j_max:
                ga_j_max = j
            

Hb, Wb = map(int, input().split())
grid_b = []
for i in range(Hb):
    inp = input()
    grid_b.append(inp)

gb_i_min = 10
gb_i_max = -1
gb_j_min = 10
gb_j_max = -1
for i in range(Hb):
    for j in range(Wb):
        if grid_b[i][j] == '#':
            if i < gb_i_min:
                gb_i_min = i
            if i > gb_i_max:
                gb_i_max = i
            if j < gb_j_min:
                gb_j_min = j
            if j > gb_j_max:
                gb_j_max = j


Hx, Wx = map(int, input().split())
grid_x = []
for i in range(Hx):
    inp = input()
    grid_x.append(inp)

gx_i_min = 10
gx_i_max = -1
gx_j_min = 10
gx_j_max = -1
for i in range(Hx):
    for j in range(Wx):
        if grid_x[i][j] == '#':
            if i < gx_i_min:
                gx_i_min = i
            if i > gx_i_max:
                gx_i_max = i
            if j < gx_j_min:
                gx_j_min = j
            if j > gx_j_max:
                gx_j_max = j


ga_tl = [ga_i_min, ga_j_min]
ga_br = [ga_i_max, ga_j_max]

gb_tl = [gb_i_min, gb_j_min]
gb_br = [gb_i_max, gb_j_max]

gx_tl = [gx_i_min, gx_j_min]
gx_br = [gx_i_max, gx_j_max]

# print()
# print()

ga_n_he = ga_br[0]-ga_tl[0]+1
ga_n_wi = ga_br[1]-ga_tl[1]+1
gb_n_he = gb_br[0]-gb_tl[0]+1
gb_n_wi = gb_br[1]-gb_tl[1]+1
gx_n_he = gx_br[0]-gx_tl[0]+1
gx_n_wi = gx_br[1]-gx_tl[1]+1

if ga_n_he > gx_n_he or ga_n_wi > gx_n_wi or gb_n_he > gx_n_he or gb_n_wi > gx_n_wi:
    print('No')
    exit()

for i1 in range(gx_n_he-ga_n_he+1):
    for j1 in range(gx_n_wi-ga_n_wi+1):
        for i2 in range(gx_n_he-gb_n_he+1):
            for j2 in range(gx_n_wi-gb_n_wi+1):
                # print(i1, j1, i2, j2)
                flag = True
                for ci in range(gx_n_he):
                    for cj in range(gx_n_wi):
                        # print(grid_x[gx_tl[0]+ci][gx_tl[1]+cj], end='')
                        if grid_x[gx_tl[0]+ci][gx_tl[1]+cj] == '#':
                            # print(gx_tl[0]+ci, gx_tl[1]+cj)
                            # print(ga_tl[0]-i1+ci, ga_tl[1]-j1+cj)
                            # print(gb_tl[0]-i2+ci, gb_tl[1]-j2+cj)
                            if 0<=ga_tl[0]-i1+ci and ga_tl[0]-i1+ci<Ha and 0<=ga_tl[1]-j1+cj and ga_tl[1]-j1+cj<Wa:
                              if grid_a[ga_tl[0]-i1+ci][ga_tl[1]-j1+cj] == '#':
                                  # print('ok1')
                                  continue
                            if 0<=gb_tl[0]-i2+ci and gb_tl[0]-i2+ci<Hb and 0<=gb_tl[1]-j2+cj and gb_tl[1]-j2+cj<Wb:
                              if grid_b[gb_tl[0]-i2+ci][gb_tl[1]-j2+cj] == '#':
                                  # print('ok2')
                                  continue
                            
                            # print('ng')
                            flag = False
                            break
                        if grid_x[gx_tl[0]+ci][gx_tl[1]+cj] == '.':
                            if 0<=ga_tl[0]-i1+ci and ga_tl[0]-i1+ci<Ha and 0<=ga_tl[1]-j1+cj and ga_tl[1]-j1+cj<Wa:
                              if grid_a[ga_tl[0]-i1+ci][ga_tl[1]-j1+cj] == '#':
                                  flag = False
                                  # print(ci, cj)
                                  break
                            if 0<=gb_tl[0]-i2+ci and gb_tl[0]-i2+ci<Hb and 0<=gb_tl[1]-j2+cj and gb_tl[1]-j2+cj<Wb:
                              if grid_b[gb_tl[0]-i2+ci][gb_tl[1]-j2+cj] == '#':
                                  flag = False
                                  # print(ci, cj)
                                  break
                    # print()
                if flag:
                    # print(i1, j1, i2, j2)
                    print('Yes')
                    exit()

print('No')