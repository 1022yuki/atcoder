import itertools

grid = []
for i in range(3):
  inp = list(map(int, input().split()))
  grid += inp 

saw = [False]*9
cnt = 0

perms = (list(itertools.permutations(range(9))))

def check_gakkari(saw, i):
  if i==0:
    if saw[3] and saw[6] and grid[3]==grid[6]:
      return True
    if saw[4] and saw[8] and grid[4]==grid[8]:
      return True
    if saw[1] and saw[2] and grid[1]==grid[2]:
      return True
  if i==1:
    if saw[4] and saw[7] and grid[4]==grid[7]:
      return True
    if saw[0] and saw[2] and grid[0]==grid[2]:
      return True
  if i==2:
    if saw[5] and saw[8] and grid[5]==grid[8]:
      return True
    if saw[0] and saw[1] and grid[0]==grid[1]:
      return True
    if saw[4] and saw[6] and grid[4]==grid[6]:
      return True
  if i==3:
    if saw[0] and saw[6] and grid[0]==grid[6]:
      return True
    if saw[4] and saw[5] and grid[4]==grid[5]:
      return True
  if i==4:
    if saw[1] and saw[7] and grid[1]==grid[7]:
      return True
    if saw[3] and saw[5] and grid[3]==grid[5]:
      return True
    if saw[0] and saw[8] and grid[0]==grid[8]:
      return True
    if saw[2] and saw[6] and grid[2]==grid[6]:
      return True
  if i==5:
    if saw[2] and saw[8] and grid[2]==grid[8]:
      return True
    if saw[3] and saw[4] and grid[3]==grid[4]:
      return True
  if i==6:
    if saw[0] and saw[3] and grid[0]==grid[3]:
      return True
    if saw[7] and saw[8] and grid[7]==grid[8]:
      return True
    if saw[4] and saw[2] and grid[4]==grid[2]:
      return True
  if i==7:
    if saw[1] and saw[4] and grid[1]==grid[4]:
      return True
    if saw[6] and saw[8] and grid[6]==grid[8]:
      return True
  if i==8:
    if saw[2] and saw[5] and grid[2]==grid[5]:
      return True
    if saw[6] and saw[7] and grid[6]==grid[7]:
      return True
    if saw[0] and saw[4] and grid[0]==grid[4]:
      return True
  return False
  
gakkari_cnt = 0
for perm in perms:
  saw_li = [False]*9
  for i in range(9):
    saw_li[perm[i]] = True
    if check_gakkari(saw_li, perm[i]):
      gakkari_cnt += 1
      break

not_gakkari = 362880 - gakkari_cnt
ans = not_gakkari/362880
print(ans)