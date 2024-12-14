import pandas as pd
import math
flare_skill_dic = [[145,153,162,171,179,188,197,205,214,223,232],
[155,164,182,192,201,210,220,220,229,238,248],
[170,180,190,200,210,221,231,241,251,261,272],
[185,196,207,218,229,240,251,262,273,284,296],
[205,217,229,241,254,266,278,291,303,315,328],
[230,243,257,271,285,299,312,326,340,354,368],
[255,270,285,300,316,331,346,362,377,392,408],
[290,307,324,342,359,377,394,411,429,446,464],
[335,355,375,395,415,435,455,475,495,515,536],
[400,424,448,472,496,520,544,568,592,616,640],
[465,492,520,548,576,604,632,660,688,716,744],
[510,540,571,601,632,663,693,724,754,785,816],
[545,577,610,643,675,708,741,773,806,839,872],
[575,609,644,678,713,747,782,816,851,885,920],
[600,636,672,708,744,780,816,852,888,924,960],
[620,657,694,731,768,806,843,880,917,954,992],
[635,673,711,749,787,825,863,901,939,977,1016],
[650,689,728,767,806,845,884,923,962,1001,1040],
[665,704,744,784,824,864,904,944,984,1024,1064]]

def flare_to_lv(flare_rank,flare_skill):
    
    for songlv in range(len(flare_skill_dic)):
        for frank,skill in enumerate(flare_skill_dic[songlv]):
            if skill==flare_skill and(frank==int(10 if flare_rank == "EX" else 0 if flare_rank == "NONE" else flare_rank) ):
                #print(f"{songlv+1},\n{frank},{skill}")
                return songlv+1
    
def score_to_sa(lv,score):
    if (score>=900000)&(str(lv).isdigit()):
        return math.floor(float(lv)*((score-900000)/50000+1)*100)/100

#スコアデータにLvなどを統合
def make_summary():
    ''' 
    説明
    ./songlv.csv:曲のlv一覧が入っている
    ./songpage_withVer.csv:曲のlv以外のデータ一覧
    ./songnotes.csv:曲のノーツ数一覧が入っている
    曲のデータに各曲のノーツ数とlvのデータを合成
    '''


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
    
    # レベル一覧から取りこぼした曲でデータ更新が可能なものには直接計算したものを入れる
    for index, row in songpage_withver.iterrows():
        if (str(row['Lv'])=='Lv') & (row['Fskill']!=0):
            print(flare_to_lv(row['Frank'],row['Fskill']),row['曲名'],row['難易度'])
            songpage_withver.at[index,'Lv']=flare_to_lv(row['Frank'],row['Fskill'])
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
    # SA列を追加して計算
    songpage_withver['SkillAttack'] = 0
    for index, row in songpage_withver.iterrows():
        songpage_withver.at[index,'SkillAttack']=score_to_sa(row['Lv'],row['SCORE'])
    # 更新されたデータを保存
    songpage_withver.to_csv('updated_songpage_withVer.csv', index=False, sep=';')
    
    print("処理が完了しました。結果は 'updated_songpage_withVer.csv' に保存されています。")
    
def make_sa_list():
    songcsv = pd.read_csv('./updated_songpage_withVer.csv', delimiter=';').sort_values('SkillAttack',ascending=False)
    Sp=0
    for index in range(30):
        sd=songcsv.iloc[index]
        SongName=sd['曲名']
        Difficulty=sd['難易度']
        Lv=sd['Lv']
        Score=sd['SCORE']
        Sa=sd['SkillAttack']
        print(f"{SongName},{Difficulty},{Lv},{Score},{Sa}")
        Sp+=Sa
    print(f"SkillPoint={Sp}")
    songcsv[:30].to_csv('DDRWORLD_SkillAttack.csv', index=False, sep=';')
make_summary()
make_sa_list()