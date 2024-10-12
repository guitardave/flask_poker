import random
import os
from datetime import datetime

from .deck_of_cards import CARDS


class SimpleCardGame:
    CARD_PATH = os.environ.get('CARD_PATH')

    def __init__(self, max_hand: int, min_hand: int, n_players: int):
        self.max_hand = max_hand
        self.min_hand = min_hand
        self.n_players = n_players
        self.cards = CARDS

    @staticmethod
    def get_card_val(card: dict) -> int:
        return int(card['value'][0])

    @staticmethod
    def get_card_face(card: dict) -> str:
        return str(card['value'][1])

    def shuffle_deck(self) -> list:
        deck = self.cards
        random.shuffle(deck)
        return deck

    def deal_hand(self) -> list[dict]:
        deck = self.shuffle_deck()
        player_cards = []
        player_calc = self.max_hand * self.n_players
        i = 0
        while i < player_calc:
            for j in range(self.n_players):
                d = deck[i]
                player_cards.append(
                    dict(
                        player=f'Player {j+1}',
                        card_face=self.get_card_face(d),
                        card_val=self.get_card_val(d),
                        card_img=self.CARD_PATH + d['img'])
                )
                i += 1

        return player_cards


class GameDetail:
    def __init__(self, max_h: int = None, min_h: int = None, n_p: int = None):
        self.max_h = max_h if max_h else 5
        self.min_h = min_h if min_h else 5
        self.n_p = n_p if n_p else 2
        self.scg = SimpleCardGame(self.max_h, self.min_h, self.n_p)

    def g_details(self) -> dict:
        return {'max_h': self.max_h, 'min_h': self.min_h, 'n_p': self.n_p}

    def g_divider(self) -> int:
        return int(12 / self.n_p)

    def g_context(self) -> dict:
        return {
            'cards': self.scg.deal_hand(),
            'year': datetime.strftime(datetime.now(), '%Y'),
            'n_players': self.scg.n_players,
            'n': self.g_divider()
        }


class CompareValues:
    def __init__(self, cards: list, max_value: int = None):
        self.cards = cards
        self.max_value = max_value if max_value else 21

    def compare(self) -> int:
        total = 0
        for card in self.cards:
            val = card['value'][0]
            total += val
        return total
