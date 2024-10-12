from card_game.simple_card_game import SimpleCardGame


class Game:

    def __init__(self, max_h: int, min_h: int, n_p: int):
        self.max_h = max_h
        self.min_h = min_h
        self.n_p = n_p

    def game_params(self):
        return {'max_hand': self.max_h, 'min_hand': self.min_h, 'n_players': self.n_p}

    def game(self):
        g_params = self.game_params()
        scg = SimpleCardGame(
            max_hand=g_params['max_hand'],
            min_hand=g_params['min_hand'],
            n_players=g_params['n_players']
        )
        return scg
