S = list(input())

# 倒れている時True

li1 = [False]
li2 = [False]
li3 = [False]*2
li4 = [False]*2
li5 = [False]*2
li6 = [False]
li7 = [False]

# 全Trueかどうか


if S[0] == '0':
  li4[0] = True
if S[1] == '0':
  li3[0] = True
if S[2] == '0':
  li5[0] = True
if S[3] == '0':
  li2[0] = True
if S[4] == '0':
  li4[1] = True
if S[5] == '0':
  li6[0] = True
if S[6] == '0':
  li1[0] = True
if S[7] == '0':
  li3[1] = True
if S[8] == '0':
  li5[1] = True
if S[9] == '0':
  li7[0] = True

if not li4[0]:
  print('No')
else:
  # ぴん1は倒れている
  if li2[0] == True:
    if li1[0] == False and (li3[0]==False or li3[1]==False or li4[0]==False or li4[1]==False or li5[0]==False or li5[1]==False or li6[0]==False or li7[0]==False):
      print('Yes')
      exit()
  if li3[0] == True and li3[1] == True:
    if (li1[0] == False or li2[0] == False) and (li4[0]==False or li4[1]==False or li5[0]==False or li5[1]==False or li6[0]==False or li7[0]==False):
      print('Yes')
      exit()
  if li4[0] == True and li4[1] == True:
    if (li1[0]==False or li2[0]==False or li3[0]==False or li3[1]==False) and(li5[0]==False or li5[1]==False or li6[0]==False or li7[0]==False):
      print('Yes')
      exit()
  if li5[0] == True and li5[1] == True:
    if (li7[0] == False or li6[0] == False) and (li4[0]==False or li4[1]==False or li3[0]==False or li3[1]==False or li2[0]==False or li1[0]==False):
      print('Yes')
      exit()
  if li6[0] == True:
    if li7[0] == False and (li5[0]==False or li5[1]==False or li4[0]==False or li4[1]==False or li3[0]==False or li3[1]==False or li2[0]==False or li1[0]==False):
      print('Yes')
      exit()
  print('No')