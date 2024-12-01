from bs4 import BeautifulSoup
from load_cookie import get_page_with_cookies

def get_tag_content_by_id(html, tag_id):
    soup = BeautifulSoup(html, 'lxml')
    # 指定されたIDを持つタグを検索
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
    url = 'https://p.eagate.573.jp/game/ddr/ddrworld/playdata/index.html'  # アクセスしたいURL
    version_name_id = 'graph_title'
    table_id = 'data_tbl'  # 取得したいタグのID

    # ページを取得
    session = get_page_with_cookies(cookie_file)
    response = session.get(url)

    html = response.text

    if html:
        # IDを指定してタグの内容を取得
        # soup = BeautifulSoup(html, 'lxml')
        # elements = soup.find_all(id="status")
        # text_parts = elements[1].get_text(separator="\n", strip=True).split("\n")
        # print(text_parts)
        status = get_tag_content_by_id(html, "status")
        # print(status)
        for n, info in enumerate(status):
            if n == 0:
                out_file_name = "status_overall.csv"
                with open(out_file_name, 'w') as out_file:
                    for i in range(0, int(len(info) / 2)):
                        # print(f"{info[2 * i]}, {info[2 * i + 1]}\n")
                        out_file.write(f"{info[2 * i]}, {info[2 * i + 1]}\n")
            else:
                out_file_name = "status_flare.csv"
                with open(out_file_name, 'w') as out_file:
                    # print(f"STYLE, {info[0]}, {info[1]}\n")
                    for i in range(1, int(len(info) / 3 + 1)):
                        # print(f"{info[3 * i - 1]}, {info[3 * i]}, {info[3 * i + 1]}\n")
                        out_file.write(f"{info[3 * i - 1]}, SINGLE, {info[3 * i]}\n")
                        out_file.write(f"{info[3 * i - 1]}, SINGLE, {info[3 * i + 1]}\n")