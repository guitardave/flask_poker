import random
import os

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

    @staticmethod
    def get_player_cards(c_list: list, card: dict) -> list[dict]:
        c_list.append(card)
        return c_list

    @staticmethod
    def get_winner(c_list: list):
        total = 0
        for c in c_list:
            total += c['value'][0]
        return total

    def draw_card(self, n: int) -> dict:
        return self.cards[n]

    def shuffle_deck(self) -> list:
        deck = self.cards
        random.shuffle(deck)
        return deck

    def deal_hand(self) -> tuple[list[dict], int]:
        deck = self.shuffle_deck()
        player_cards = []
        i = 0
        while i < self.max_hand * self.n_players:
            for j in range(self.n_players):
                d = deck[i]
                player_cards.append(
                    dict(
                        player=f'Player {j+1}',
                        card_face=self.get_card_face(d),
                        card_val=self.get_card_val(d),
                        card_img=d['img'])
                )
                i += 1
        return player_cards, i
