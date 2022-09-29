A, B, C = map(int, input().split())

# if A**C < B**C:
#   print('<')
# elif A**C > B**C:
#   print('>')
# else:
#   print('=')

if A>0 and B>0:
  if A>B:
    print('>')
  elif A==B:
    print('=')
  else:
    print('<')
elif A==0 and B==0:
  print('=')
elif A<0 and B<0:
  if C%2==0:
    if A<B:
      print('>')
    elif A==B:
      print('=')
    else:
      print('<')
  else:
    if A<B:
      print('<')
    elif A == B:
      print('=')
    else:
      print('>')
elif A == 0:
  if B > 0:
    print('<')
  else:
    if C%2 == 0:
      print('<')
    else:
      print('>')
elif B == 0:
  if A > 0:
    print('>')
  else:
    if C%2 == 0:
      print('>')
    else:
      print('<')
elif A>0 and B<0:
  if C % 2 == 1:
    print('>')
  else:
    if abs(A)>abs(B):
      print('>')
    elif abs(A)==abs(B):
      print('=')
    else:
      print('<')
elif A<0 and B>0:
  if C % 2 == 1:
    print('<')
  else:
    if abs(A)>abs(B):
      print('>')
    elif abs(A)==abs(B):
      print('=')
    else:
      print('<')

# if C % 2 == 0:
#   if abs(A) > abs(B):
#     print('>')
#   elif abs(A) < abs(B):
#     print('<')
#   else:
#     print('=')
# else:
#   if A>0 and B>0:
#     if A>B:
#       print('>')
#     elif A<B:
#       print('<')
#     else:
#       print('=')
#   elif A==0 and B==0:
#     print('=')
#   elif A<0 and B<0:
#     if A>B:
#       print('>')
#     elif A<B:
#       print('<')
#     else:
#       print('=')
  