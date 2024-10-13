import random
import os

from .deck_of_cards import CARDS


class SimpleCardGame:
    CARD_PATH = os.environ.get('CARD_PATH')
    DECK_SIZE = 52
    MAX_SCORE = 21

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

    def get_player_card_lists(self) -> list:
        return [(n, []) for n in range(self.n_players)]

    def draw_card(self, n: int, deck: list) -> dict:
        return deck[n + 1] if n < self.DECK_SIZE else {}

    def shuffle_deck(self) -> list[dict]:
        deck = self.cards
        random.shuffle(deck)
        return deck

    def deal_hand(self) -> tuple[list[dict], int, list[dict]]:
        deck, card_lists, cards_dealt, i = self.shuffle_deck(), self.get_player_card_lists(), [], 0

        while i < self.max_hand * self.n_players:
            for j in range(self.n_players):
                card = deck.__getitem__(i)
                card_lists[j][1].append(self.get_card_val(card))
                cards_dealt.append(
                    dict(
                        player=f'Player {j + 1}',
                        card_face=self.get_card_face(card),
                        card_val=self.get_card_val(card),
                        card_img=card['img'],
                        card_slug=card['slug']
                    )
                )
                i += 1
        # print(card_lists)
        return cards_dealt, i, card_lists

    @staticmethod
    def get_score(c_list: list) -> int:
        score = 0
        for c in c_list:
            score += c
        return score

    def get_winner(self, card_lists: list) -> tuple[int, int]:
        players = [(n, self.get_score(card_lists[n][1])) for n in range(self.n_players)]
        players.sort(key=lambda x: x[1], reverse=True)
        return players[0] if players[0][1] <= self.MAX_SCORE else players[1]
