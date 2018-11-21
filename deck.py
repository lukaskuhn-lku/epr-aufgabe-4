import random
from card import Card
from player import Player

class Deck:
    def __init__(self):
        self.cards = [Card("7", "Herz"),Card("8", "Herz"),Card("9", "Herz"),Card("10", "Herz"),Card("Bube", "Herz"),Card("Dame", "Herz"),Card("Koenig", "Herz"),Card("Ass", "Herz"),
                      Card("7", "Karo"),Card("8", "Karo"),Card("9", "Karo"),Card("10", "Karo"),Card("Bube", "Karo"),Card("Dame", "Karo"),Card("Koenig", "Karo"),Card("Ass", "Karo"),
                      Card("7", "Pik"),Card("8", "Pik"),Card("9", "Pik"),Card("10", "Pik"),Card("Bube", "Pik"),Card("Dame", "Pik"),Card("Koenig", "Pik"),Card("Ass", "Pik"),
                      Card("7", "Kreuz"),Card("8", "Kreuz"),Card("9", "Kreuz"),Card("10", "Kreuz"),Card("Bube", "Kreuz"),Card("Dame", "Kreuz"),Card("Koenig", "Kreuz"),Card("Ass", "Kreuz")]
        
    def returnShuffledCards(self):
        return random.shuffle(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        #return self

    def give_players_cards(self,players):
        for player in players:
            player.cards = self.cards[-3:]
            del self.cards[-3:]
        return players

    def remove_card(self, value, color):
        for card in self.cards:
            if card.value == value:
             if card.color == color:
                self.cards.remove(card)




        
    


