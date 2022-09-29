s1 = input()
s2 = input()

if s1.count('#')+s2.count('#')>=3 or s1.count('#')==2 or s2.count('#')==2:
  print('Yes')
elif s1[0]=='#' and s2[0]=='#' or s1[1]=='#' and s2[1]=='#':
  print('Yes')
else:
  print('No')