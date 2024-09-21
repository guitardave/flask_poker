import random
import os
from deck_of_cards import CARDS


class Poker:
    CARD_PATH = os.environ.get('CARD_PATH')
    MAX_HAND = 5
    REP = 4

    def __init__(self):
        pass

    @staticmethod
    def shuffle_deck():
        deck = CARDS
        random.shuffle(deck)
        return deck

    def deal_hand(self):
        deck = self.shuffle_deck()
        i = 0
        all_players = []
        while i < self.MAX_HAND * self.REP:
            for j in range(self.REP):
                d = deck[i]
                all_players.append(
                    dict(
                        player=f'Player {j+1}',
                        card_face=d[0],
                        card_val=d[1],
                        card_img=self.CARD_PATH + d[2])
                )
                i += 1

        return all_players
