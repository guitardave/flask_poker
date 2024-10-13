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
    dict(suit=CardSuit.SPADES, value=CardVal.A, img='spades_ace.svg', slug='ace-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.K, img='spades_king.svg', slug='king-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.Q, img='spades_queen.svg', slug='queen-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.J,  img='spades_jack.svg', slug='jack-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.TEN, img='spades_10.svg', slug='10-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.NINE, img='spades_9.svg', slug='9-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.EIGHT, img='spades_8.svg', slug='8-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.SEVEN, img='spades_7.svg', slug='7-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.SIX, img='spades_6.svg', slug='6-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.FIVE, img='spades_5.svg', slug='5-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.FOUR, img='spades_4.svg', slug='4-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.THREE, img='spades_3.svg', slug='3-of-spades'),
    dict(suit=CardSuit.SPADES, value=CardVal.TWO, img='spades_2.svg', slug='2-of-spades'),
    dict(suit=CardSuit.HEARTS, value=CardVal.A, img='hearts_ace.svg', slug='ace-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.K, img='hearts_king.svg', slug='king-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.Q, img='hearts_queen.svg', slug='queen-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.J, img='hearts_jack.svg', slug='jack-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.TEN, img='hearts_10.svg', slug='10-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.NINE, img='hearts_9.svg', slug='9-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.EIGHT, img='hearts_8.svg', slug='8-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.SEVEN, img='hearts_7.svg', slug='7-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.SIX, img='hearts_6.svg', slug='6-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.FIVE, img='hearts_5.svg', slug='5-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.FOUR, img='hearts_4.svg', slug='4-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.THREE, img='hearts_3.svg', slug='3-of-hearts'),
    dict(suit=CardSuit.HEARTS, value=CardVal.TWO, img='hearts_2.svg', slug='2-of-hearts'),
    dict(suit=CardSuit.CLUBS, value=CardVal.A, img='clubs_ace.svg', slug='ace-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.K, img='clubs_king.svg', slug='king-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.Q, img='clubs_queen.svg', slug='queen-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.J, img='clubs_jack.svg', slug='jack-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.TEN, img='clubs_10.svg', slug='10-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.NINE, img='clubs_9.svg', slug='9-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.EIGHT, img='clubs_8.svg', slug='8-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.SEVEN, img='clubs_7.svg', slug='7-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.SIX, img='clubs_6.svg', slug='6-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.FIVE, img='clubs_5.svg', slug='5-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.FOUR, img='clubs_4.svg', slug='4-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.THREE, img='clubs_3.svg', slug='3-of-clubs'),
    dict(suit=CardSuit.CLUBS, value=CardVal.TWO, img='clubs_2.svg', slug='2-of-clubs'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.A, img='diamonds_ace.svg', slug='ace-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.K, img='diamonds_king.svg', slug='king-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.Q, img='diamonds_queen.svg', slug='queen-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.J, img='diamonds_jack.svg', slug='jack-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.TEN, img='diamonds_10.svg', slug='10-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.NINE, img='diamonds_9.svg', slug='9-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.EIGHT, img='diamonds_8.svg', slug='8-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.SEVEN, img='diamonds_7.svg', slug='7-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.SIX, img='diamonds_6.svg', slug='6-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.FIVE, img='diamonds_5.svg', slug='5-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.FOUR, img='diamonds_4.svg', slug='4-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.THREE, img='diamonds_3.svg', slug='3-of-diamonds'),
    dict(suit=CardSuit.DIAMONDS, value=CardVal.TWO, img='diamonds_2.svg', slug='2-of-diamonds'),
]
