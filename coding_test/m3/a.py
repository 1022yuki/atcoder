import sys

# 単語を保持するリスト
Words = []
# 各業を受け取りながら単語ごとにWordsに追加する
for line in sys.stdin:
    li_line = list(map(str, line.strip().split()))
    Words += li_line

# 単語中の.,!?などを削除
for i in range(len(Words)):
    Words[i] = Words[i].replace('.', '')
    Words[i] = Words[i].replace(',', '')
    Words[i] = Words[i].replace('!', '')
    Words[i] = Words[i].replace('?', '')

# Words内の重複を削除
Words = list(set(Words))

# 単語の先頭が大文字もしくは数字かどうかを効率的に判定するためのset
target = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

ans = 0
for word in Words:
    if word[0] in target:
        ans += 1

print(ans)