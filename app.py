import os

from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from flask_cors import CORS, cross_origin

from card_game.simple_card_game import GameDetail

from forms import GameForm


class App:
    def __init__(self):
        self.app = Flask(__name__)

    def create_app(self):
        self.app.secret_key = os.environ.get('SECRET_KEY')
        CORS(self.app)
        csrf = CSRFProtect(self.app)
        csrf.init_app(self.app)
        return self.app


app = App().create_app()
app.config.from_object('config')
app.config['SESSION_COOKIE_SECURE'] = False


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    game_d = GameDetail()
    form = GameForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            r_game = request.form.get('game')
            p_game = r_game.split(',')
            game_max_h = int(p_game[0])
            game_min_h = int(p_game[1])
            n_players = int(request.form.get('n_players'))
            game_d = GameDetail(game_max_h, game_min_h, n_players)
    context = {'title': 'Idiot Dave Card Game', 'form': GameForm(), **game_d.g_context()}
    return render_template('index.html', **context)


@app.route('/shuffle/', methods=['GET', 'POST'])
@app.route('/shuffle/<int:max_h>/<int:min_h>/<int:n_p>/', methods=['GET', 'POST'])
@cross_origin()
def shuffle_n_deal_async(max_h: int = None, min_h: int = None, n_p: int = None):
    game_d = GameDetail(max_h, min_h, n_p)
    context = game_d.g_context()
    return render_template('game_board_partial.html', **context)


if __name__ == '__main__':
    app.run()
