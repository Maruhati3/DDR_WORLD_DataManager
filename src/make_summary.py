import pandas as pd

# CSVファイルを読み込む（区切り文字を指定）
songlv = pd.read_csv('./songlv.csv', delimiter=';;')
songpage_withver = pd.read_csv('./songpage_withVer.csv', delimiter=';')
songnotes = pd.read_csv('./songnotes.csv', delimiter=';')

# 難易度と対応する列名のマッピング
difficulty_map_lv = {
    "beginner": "bSP",
    "basic": "BSP",
    "difficult": "DSP",
    "expert": "ESP",
    "challenge": "CSP"
}

difficulty_map_notes = {
    "beginner": "bSP",
    "basic": "BSP",
    "difficult": "DSP",
    "expert": "ESP",
    "challenge": "CSP"
}

# Lv列の更新
for index, row in songpage_withver.iterrows():
    if row['SPDP'] == "SP":  # SPDPがSPの場合
        difficulty = row['難易度']  # 難易度を取得
        if difficulty in difficulty_map_lv:  # 難易度がマッピングに存在する場合
            column_name_lv = difficulty_map_lv[difficulty]  # songlvの列名を取得
            # 曲名を基に対応する値を取得
            matching_row_lv = songlv[songlv['曲名'] == row['曲名']]
            if not matching_row_lv.empty:  # 一致する曲名が存在する場合
                songpage_withver.at[index, 'Lv'] = matching_row_lv.iloc[0][column_name_lv]  # Lv列を更新

# Notes列を追加
songpage_withver['Notes'] = None

# Notes列の更新
for index, row in songpage_withver.iterrows():
    if row['SPDP'] == "SP":  # SPDPがSPの場合
        difficulty = row['難易度']  # 難易度を取得
        if difficulty in difficulty_map_notes:  # 難易度がマッピングに存在する場合
            column_name_notes = difficulty_map_notes[difficulty]  # songnotesの列名を取得
            # 曲名を基に対応する値を取得
            matching_row_notes = songnotes[songnotes['曲名'] == row['曲名']]
            if not matching_row_notes.empty:  # 一致する曲名が存在する場合
                songpage_withver.at[index, 'Notes'] = matching_row_notes.iloc[0][column_name_notes]  # Notes列を更新

# 更新されたデータを保存
songpage_withver.to_csv('updated_songpage_withVer.csv', index=False, sep=';')

print("処理が完了しました。結果は 'updated_songpage_withVer.csv' に保存されています。")
