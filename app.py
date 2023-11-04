from flask import Flask, render_template,jsonify, request
import os

app = Flask(__name__)

# ゲームボードの初期状態（仮の例）
board = [[1, 1, -1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

# 各セルのクラスを設定するための辞書
cell_class = {1: 'red', -1: 'yellow', 0: 'white'}

@app.route('/')
def connect4():
    return render_template('board.html', board=np.transpose(board), cell_class=cell_class)

@app.route('/get_board')
def get_board():
    return jsonify({'board': board})

@app.route('/update_board', methods=['POST'])
def update_board():
    data = request.get_json()
    updated_board = data['board']  # クライアントからのデータを受け取り

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    app.run()
