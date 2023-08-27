import csv
import sys
from statistics import mean

# CSVリーダーを作成
reader = csv.reader(sys.stdin)

# 最初の行 (ヘッダー) を取得
headers = next(reader)

# 各科目のスコアを保存するための辞書を初期化
scores = {header: [] for header in headers}

# 各行を処理
for row in reader:
    for header, score in zip(headers, row):
        # スコアを整数に変換して辞書に追加
        scores[header].append(int(score))

# 平均を計算し、出力
averages = [mean(scores[header]) for header in headers]
print(','.join(headers))
print(','.join(map(str, map(round, averages))))