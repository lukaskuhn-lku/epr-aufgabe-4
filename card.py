class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def can_card_be_put_on_top(self,tmp_card):
        if tmp_card.value == self.value:
            return True
        elif tmp_card.color == self.color:
            return True
        else:
            return False

