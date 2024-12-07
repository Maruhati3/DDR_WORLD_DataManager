from bs4 import BeautifulSoup
from flare_rank import flare_rank
from load_cookie import get_page_with_cookies

def get_tag_content_by_id(html, tag_id):
    soup = BeautifulSoup(html, 'lxml')
    # 指定されたIDを持つタグを検索
    # tag = soup.find(id=tag_id)
    # tags = soup.find_all(id=tag_id)

    # if tag:
    #     return tag.text.strip()
    # if tags:
    #     return [tag.text.strip().split() for tag in tags]
    # else:
    #     print(f"Tag with ID {tag_id} not found.")
    #     return None
    # 結果を格納するリスト
    # IDを持つ全ての要素をリストで取得
    elements = soup.find_all(id=tag_id)
    
    results = []
    
    for tag in elements:
        result = []
        # タグ内のテキストを <br> で分割
        text_parts = tag.get_text(separator="\n", strip=True).split("\n")
        
        # 分割されたテキスト部分を結果リストに追加
        result.extend(text_parts)
        # print(result)
        results.append(result)

    # print(results)
    return results
    
def get_tag_content_by_classname(html, tag_class):
    soup = BeautifulSoup(html, 'lxml')
    # 指定されたIDを持つタグを検索
    # tag = soup.find(id=tag_id)
    tags = soup.find_all(class_=tag_class)

    if tags:
        return [tag.text.strip().split() for tag in tags]
    else:
        print(f"Tag with ID {tag_class} not found.")
        return None

if __name__ == "__main__":
    # 使用例
    cookie_file = './cookie.pkl'  # 保存したクッキーのファイル
    url = 'https://p.eagate.573.jp/game/ddr/ddrworld/playdata/flare_data_single.html'  # アクセスしたいURL
    version_name_id = 'graph_title'
    table_id = 'data_tbl'  # 取得したいタグのID

    # ページを取得
    session = get_page_with_cookies(cookie_file)
    response = session.get(url)

    html = response.text

    if html:
        # IDを指定してタグの内容を取得
        # content = get_tag_content_by_id(html, tag_id)
        versions = get_tag_content_by_classname(html, version_name_id)
        tables = get_tag_content_by_id(html, table_id)

        if tables:
            idx = 0

            out_file_name = "flare_output.csv"
            with open(out_file_name, "w", encoding="utf-8") as out_file:
                for version, table in zip(versions, tables):
                    #print(table)
                    if idx == 0:
                        # print("バージョン;楽曲名;難易度;レベル;フレアランク;フレアスキル;プレー日時\n")
                        # out_file.write("バージョン;楽曲名;難易度;レベル;フレアランク;フレアスキル;プレー日時\n")
                        out_file.write("Version;Title;Difficulty;Level;Flare Rank;Flare Skill;Play Date\n")
                    for i in range(1, int((len(table) - 1) / 5)):
                        idx += 1
                        chart_lv = table[5 * i + 3]
                        lv = chart_lv.split(".")[1]
                        flare_skill = table[5 * i + 4]
                        rank = flare_rank(int(lv), int(flare_skill))
                        # print(f"{version[0]};{table[5 * i + 1]};{table[5 * i + 2]};{table[5 * i + 3]};{table[5 * i + 4]};{table[5 * i + 5]}\n")
                        out_file.write(f"{version[0]};{table[5 * i + 1]};{table[5 * i + 2]};{chart_lv};{rank};{flare_skill};{table[5 * i + 5]}\n")
