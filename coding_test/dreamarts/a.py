s = input()

if 'img' in s and 'doc' in s:
    print('presentation')
elif 'img' in s:
    print('image')
elif 'doc' in s:
    print('document')
else:
    print('other')