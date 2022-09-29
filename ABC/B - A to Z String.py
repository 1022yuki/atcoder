import re

s = input()

tar = re.search(r'A[A-Z]*Z', s)

print(len(tar.group()))