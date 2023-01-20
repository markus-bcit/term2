

class Card:
    def __init__(self, value, color):
        if value > 10 or value <= 0:
            raise AttributeError
        
        self.value = value
        if color not in ('red', 'black'):
            raise AttributeError
        
        self.color = color
        
    def is_stronger_than(self, other_card):
        
        return self.value > other_card.value

