class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle_deck(self):
        import random
        random.shuffle(self.cards)


# Usage:
new_deck = Deck()
print(new_deck.cards)
new_deck.shuffle_deck()
print(new_deck.cards)
print("-" * 80)
print(f"Last card: {new_deck.cards[-1]}")

