from flask import Flask, render_template
from poker import Poker


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    poker = Poker()
    return render_template('index.html', cards=poker.deal_hand())


@app.route('/shuffle/')
def shuffle():
    poker = Poker()
    poker.shuffle_deck()
    return render_template('game_board_partial.html', cards=poker.deal_hand())


if __name__ == '__main__':
    app.run()
