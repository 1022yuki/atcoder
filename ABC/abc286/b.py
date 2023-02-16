import re
N = int(input())
S = input()

ans = re.sub("na", "nya", S)
print(ans)