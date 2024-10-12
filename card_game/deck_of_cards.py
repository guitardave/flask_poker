"""
    DECK OF CARDS
    DAVE CRANDELL 2024
    52-CARD DECK DEFINED AS DICT
    IMAGES AT https://jojodave.s3.amazonaws.com/static/cards/
"""


class CardSuit:
    SPADES = 'Spades'
    CLUBS = 'Clubs'
    DIAMONDS = 'Diamonds'
    HEARTS = 'Hearts'


class CardVal:
    A = 11, 'A'
    K = 10, 'K'
    Q = 10, 'Q'
    J = 10, 'J'
    TEN = 10, '10'
    NINE = 9, '9'
    EIGHT = 8, '8'
    SEVEN = 7, '7'
    SIX = 6, '6'
    FIVE = 5, '5'
    FOUR = 4, '4'
    THREE = 3, '3'
    TWO = 2, '2'
    

CARDS = [
    dict(suit=CardSuit.SPADES, value=CardVal.A, img='Spades_A.jpg', slug='ace-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.K, img='Spades_K.jpg', slug='king-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.Q, img='Spades_Q.jpg', slug='queen-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.J,  img='Spades_J.jpg', slug='jack-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.TEN, img='Spades_10.jpg', slug='10-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.NINE, img='Spades_9.jpg', slug='9-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.EIGHT, img='Spades_8.jpg', slug='8-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.SEVEN, img='Spades_7.jpg', slug='7-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.SIX, img='Spades_6.jpg', slug='6-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.FIVE, img='Spades_5.jpg', slug='5-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.FOUR, img='Spades_4.jpg', slug='4-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.THREE, img='Spades_3.jpg', slug='3-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.TWO, img='Spades_2.jpg', slug='2-of-spades'),
    dict(suit=CardSuit.HEARTS, value=CardVal.A, img='Hearts_A.jpg', slug='ace-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.K, img='Hearts_K.jpg', slug='king-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.Q, img='Hearts_Q.jpg', slug='queen-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.J, img='Hearts_J.jpg', slug='jack-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.TEN, img='Hearts_10.jpg', slug='10-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.NINE, img='Hearts_9.jpg', slug='9-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.EIGHT, img='Hearts_8.jpg', slug='8-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.SEVEN, img='Hearts_7.jpg', slug='7-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.SIX, img='Hearts_6.jpg', slug='6-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.FIVE, img='Hearts_5.jpg', slug='5-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.FOUR, img='Hearts_4.jpg', slug='4-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.THREE, img='Hearts_3.jpg', slug='3-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.TWO, img='Hearts_2.jpg', slug='2-of-hearts'),
    dict(suit=CardSuit.CLUBS, value=CardVal.A, img='Clubs_A.jpg', slug='ace-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.K, img='Clubs_K.jpg', slug='king-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.Q, img='Clubs_Q.jpg', slug='queen-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.J, img='Clubs_J.jpg', slug='jack-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.TEN, img='Clubs_10.jpg', slug='10-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.NINE, img='Clubs_9.jpg', slug='9-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.EIGHT, img='Clubs_8.jpg', slug='8-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.SEVEN, img='Clubs_7.jpg', slug='7-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.SIX, img='Clubs_6.jpg', slug='6-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.FIVE, img='Clubs_5.jpg', slug='5-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.FOUR, img='Clubs_4.jpg', slug='4-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.THREE, img='Clubs_3.jpg', slug='3-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.TWO, img='Clubs_2.jpg', slug='2-of-clubs'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.A, img='Diamonds_A.jpg', slug='ace-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.K, img='Diamonds_K.jpg', slug='king-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.Q, img='Diamonds_Q.jpg', slug='queen-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.J, img='Diamonds_J.jpg', slug='jack-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.TEN, img='Diamonds_10.jpg', slug='10-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.NINE, img='Diamonds_9.jpg', slug='9-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.EIGHT, img='Diamonds_8.jpg', slug='8-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.SEVEN, img='Diamonds_7.jpg', slug='7-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.SIX, img='Diamonds_6.jpg', slug='6-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.FIVE, img='Diamonds_5.jpg', slug='5-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.FOUR, img='Diamonds_4.jpg', slug='4-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.THREE, img='Diamonds_3.jpg', slug='3-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.TWO, img='Diamonds_2.jpg', slug='2-of-diamonds'),
]
