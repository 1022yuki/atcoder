import re

s = input()

# 正規表現パターンを作成
pattern = r"Postcode: (\d{3})-(\d{4})"

# 入力された文字列から一致する文字列を抽出
matche_obj = re.search(pattern, s)

# 抽出した文字列を出力
if matche_obj:
    print(matche_obj.group(1)+matche_obj.group(2))
else:
    print("FORMAT ERROR")