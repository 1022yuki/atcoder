import re

inp = list(map(str, input().split()))

m = int(inp[-1])

Num_word = []
lg = len(inp)-1
for i in range(lg):
    num_word = inp[i]
    num = int(re.sub(':.*', '', num_word))
    word = re.sub('.*:', '', num_word)
    Num_word.append([num, word])

Num_word.sort()
# print(Num_word)
ans = []
for i in range(lg):
    if m % Num_word[i][0] == 0:
        ans.append(Num_word[i][1])

print(''.join(ans) if ans else m)