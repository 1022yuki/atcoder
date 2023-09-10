S = input()
import re
ans = re.sub('[aiueo]', '', S)
print(ans)