from flask_wtf import CSRFProtect, FlaskForm
from wtforms import SelectField
from wtforms.fields.simple import SubmitField


class GameForm(FlaskForm):
    class Players:
        N_PLAYERS = [('2', '2'), ('3', '3'), ('4', '4'), ('6', '6')]

    class GameList:
        GAME_LIST = [
            ('2,2', 'Blackjack'),
            # ('5,5', '5-Card Stud')
        ]

    n_players = SelectField(label='Number of Players', choices=Players.N_PLAYERS)
    game = SelectField(label='Type of Game', choices=GameList.GAME_LIST)
    submit = SubmitField(label='Go')
