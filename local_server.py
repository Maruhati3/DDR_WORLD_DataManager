from flask import Flask, render_template, jsonify, request
import pandas as pd

app = Flask(__name__)

# CSVファイルの読み込み
def load_csv(file_name):
    df = pd.read_csv(file_name, sep=';')  # あなたのCSVファイル名
    return df

@app.route('/')
def index():
    return render_template('index.html')

# CSVデータをJSONとして返すエンドポイント
@app.route('/get_data', methods=['GET'])
def get_data():
    test_file_name = "flare_output.csv"
    df = load_csv(test_file_name)

    # print(df.columns)
    
    # フィルタリングやソートなどの処理
    # 例えば、クエリパラメータでソートやフィルタリングする場合
    # column = request.args.get('column', default='column_name', type=str)
    column = request.args.get('column', default='Version' , type=str)
    order = request.args.get('order', default='asc', type=str)
    
    #if order == 'desc':
    #    df = df.sort_values(by=column, ascending=False)
    #else:
    #    df = df.sort_values(by=column, ascending=True)

    response = jsonify(df.to_dict(orient='records'))
    print(response)
    # データをJSONとして返す
    return response
    # return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)