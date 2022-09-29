N = input()

state = False

if N[0] == '7':
  state = True
if N[1] == '7':
  state = True
if N[2] == '7':
  state = True

if state:
  print('Yes')
else:
  print('No')