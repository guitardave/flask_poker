from flask import Flask, render_template
import random
import os


card_path = os.environ.get('CARD_PATH')
cards = [
    ('Spades', 'A', 'Spades_A.jpg'),
    ('Spades', 'K', 'Spades_K.jpg'),
    ('Spades', 'Q', 'Spades_Q.jpg'),
    ('Spades', 'J', 'Spades_J.jpg'),
    ('Spades', '10', 'Spades_10.jpg'),
    ('Spades', '9', 'Spades_9.jpg'),
    ('Spades', '8', 'Spades_8.jpg'),
    ('Spades', '7', 'Spades_7.jpg'),
    ('Spades', '6', 'Spades_6.jpg'),
    ('Spades', '5', 'Spades_5.jpg'),
    ('Spades', '4', 'Spades_4.jpg'),
    ('Spades', '3', 'Spades_3.jpg'),
    ('Spades', '2', 'Spades_2.jpg'),
    ('Hearts', 'A', 'Hearts_A.jpg'),
    ('Hearts', 'K', 'Hearts_K.jpg'),
    ('Hearts', 'Q', 'Hearts_Q.jpg'),
    ('Hearts', 'J', 'Hearts_J.jpg'),
    ('Hearts', '10', 'Hearts_10.jpg'),
    ('Hearts', '9', 'Hearts_9.jpg'),
    ('Hearts', '8', 'Hearts_8.jpg'),
    ('Hearts', '7', 'Hearts_7.jpg'),
    ('Hearts', '6', 'Hearts_6.jpg'),
    ('Hearts', '5', 'Hearts_5.jpg'),
    ('Hearts', '4', 'Hearts_4.jpg'),
    ('Hearts', '3', 'Hearts_3.jpg'),
    ('Hearts', '2', 'Hearts_2.jpg'),
    ('Clubs', 'A', 'Clubs_A.jpg'),
    ('Clubs', 'K', 'Clubs_K.jpg'),
    ('Clubs', 'Q', 'Clubs_Q.jpg'),
    ('Clubs', 'J', 'Clubs_J.jpg'),
    ('Clubs', '10', 'Clubs_10.jpg'),
    ('Clubs', '9', 'Clubs_9.jpg'),
    ('Clubs', '8', 'Clubs_8.jpg'),
    ('Clubs', '7', 'Clubs_7.jpg'),
    ('Clubs', '6', 'Clubs_6.jpg'),
    ('Clubs', '5', 'Clubs_5.jpg'),
    ('Clubs', '4', 'Clubs_4.jpg'),
    ('Clubs', '3', 'Clubs_3.jpg'),
    ('Clubs', '2', 'Clubs_2.jpg'),
    ('Diamonds', 'A', 'Diamonds_A.jpg'),
    ('Diamonds', 'K', 'Diamonds_K.jpg'),
    ('Diamonds', 'Q', 'Diamonds_Q.jpg'),
    ('Diamonds', 'J', 'Diamonds_J.jpg'),
    ('Diamonds', '10', 'Diamonds_10.jpg'),
    ('Diamonds', '9', 'Diamonds_9.jpg'),
    ('Diamonds', '8', 'Diamonds_8.jpg'),
    ('Diamonds', '7', 'Diamonds_7.jpg'),
    ('Diamonds', '6', 'Diamonds_6.jpg'),
    ('Diamonds', '5', 'Diamonds_5.jpg'),
    ('Diamonds', '4', 'Diamonds_4.jpg'),
    ('Diamonds', '3', 'Diamonds_3.jpg'),
    ('Diamonds', '2', 'Diamonds_2.jpg'),
]

app = Flask(__name__)


def shuffle_deck():
    deck = cards
    random.shuffle(deck)
    return deck


def deal_hand():
    deck = shuffle_deck()
    max_hand = 5
    i = 0
    rep = 4
    all_players = []
    while i < max_hand * rep:
        for j in range(rep):
            d = deck[i]
            all_players.append(dict(player=f'Player {j+1}', card_face=d[0], card_val=d[1], card_img=card_path + d[2]))
            i += 1

    return all_players


@app.route('/')
def index():  # put application's code here
    all_players = deal_hand()
    return render_template('index.html', cards=all_players)


if __name__ == '__main__':
    app.run()
