class Deck:

    def __init__(self):

        self.cards = []

    def add(self, card: str):
        self.cards.append(card)
    
    def remove(self, card: str):
        self.cards.remove(card)

    def number(self) -> int:
        return len(self.cards)
    
    def cards_list(self) -> str:
        c_list = " ".join(self.cards)
        return c_list
