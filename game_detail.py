from datetime import datetime

from card_game.simple_card_game import SimpleCardGame


class GameDetail:
    def __init__(self, max_h: int = None, min_h: int = None, n_p: int = None):
        self.max_h = max_h if max_h else 2
        self.min_h = min_h if min_h else 2
        self.n_p = n_p if n_p else 4
        self.scg = SimpleCardGame(self.max_h, self.min_h, self.n_p)

    def g_divider(self) -> int:
        return int(12 / self.n_p)

    def g_context(self) -> dict:
        scg = self.scg.deal_hand()
        return {
            'cards': scg[0],
            'n_cards': scg[1],
            'card_lists': scg[2],
            'year': datetime.strftime(datetime.now(), '%Y'),
            'n_players': self.scg.n_players,
            'n': self.g_divider(),
            'winner': self.scg.get_winner(scg[2])[0]
        }
