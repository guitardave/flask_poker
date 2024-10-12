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
