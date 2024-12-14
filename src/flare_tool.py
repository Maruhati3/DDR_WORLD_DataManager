import pandas as pd
import sys
args = sys.argv
# CSVの読み込み
flare_data = pd.read_csv('flare_output.csv', delimiter=';')
print(flare_data)
# 区間の指定
ranges = [
    (1, 30),  # 1〜30行目
    (31, 60), # 31〜60行目
    (61, 90)  # 61〜90行目
]


# 結果を格納する辞書
flare_skill_counts = {}

# 各区間に対する処理
for start, end in ranges:
    # pandasのインデックスは0ベースなので-1する
    subset = flare_data.iloc[start-1:end]
    
    # フレアスキル列の値をカウント
    counts = dict(sorted(subset['フレアスキル'].value_counts().to_dict().items(),key=lambda item:item[0],reverse=True))
    
    # 区間ごとのカウントを辞書に保存
    flare_skill_counts[f"{start}"] = counts

def under(version):
    if len(args)==1:
        return 0
    elif len(args)>=3 and args[1]==version:
        return args[2]
    else:
        return 0
# 結果を表示
allsum=0
allifsum=0
for section, counts in flare_skill_counts.items():
    print(f"区間 {section} のフレアスキルカウント:")
    sum=0
    #引数が十分にある場合下限機能起動
        
    for skill, count in counts.items():
        print(f"Skill{skill}: {count}回")
        sum+=skill*count
        allsum+=skill*count
        allifsum+=max(int(under(section)),skill)*count
        
print(allsum)
print(allifsum)