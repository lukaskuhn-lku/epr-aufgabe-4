from player import Player
from deck import Deck 
from card import Card
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#User Eingaben zum Game
player_count = 0
while not player_count >= 2 | player_count < 5:
    try:
        player_count = int(input("Bitte eine Spieleranzahl zwischen 2 - 4 angeben: "))
    except:
        player_count = 0

players = []
for count in range(player_count):
    try:
        print("Bitte geben Sie einen Namen fuer Spieler ",count+1," ein: ")
        player_name = input()
        tmp_player = Player(player_name, None)
        players.append(tmp_player)
    except:
        print("Fehler bei der Eingabe der Spielernamen")



#print("Deck Ausgabe: ")
#for card in deck.cards:
#    print(card.value, card.symbol)

game_status = "playing"
current_player_count = 0
deck = Deck()
deck.shuffle()

players = deck.give_players_cards(players)
top_card = deck.cards.pop()

def create_new_deck():
        print("Neues Deck wird erzeugt")
        deck = Deck()
        deck.shuffle()
        for player in players:
            for card in player.cards:
                deck.remove_card(card.value, card.color)
        deck.remove_card(top_card.value, top_card.color)
        return deck

def show_top_card():
    print("Aufgedeckte Karte: ", top_card.value, top_card.color)

def show_current_player_cards():
    counter = 1
    for card in current_player.cards:
        print("Karte ",counter, " : ", card.value, card.color)
        counter += 1

while game_status == "playing":
    if len(deck.cards) == 0:
        deck = create_new_deck()
    
    cls()

    if current_player_count >= len(players):
        current_player_count = 0

    show_top_card()

    current_player = players[current_player_count]
    print(current_player.name)
    show_current_player_cards()
    
    for player in players:
        if player.name != current_player.name:
            print("Spieler ", player.name, " hat noch ", len(player.cards), " Karten")

    player_has_playable_card = False
    for card in current_player.cards:
        if top_card.can_card_be_put_on_top(card):
            player_has_playable_card = True
    
    if not player_has_playable_card:
        print("Es wird automatisch eine Karte gezogen, da keine spielbare Karte vorhanden ist")
        card = deck.cards.pop()
        current_player.cards.append(card)
        print("Neu gezogene Karte: ", card.value, card.color)
    else:
        player_wants_card = input("Moechtest du eine neue Karte ziehen? (j/n): ")
        if player_wants_card == "j":
            card = deck.cards.pop()
            current_player.cards.append(card)
            print("Neu gezogene Karte: ", card.value, card.color)
        else: 
            cls()
   
    player_has_playable_card = False
    for card in current_player.cards:
        if top_card.can_card_be_put_on_top(card):
            player_has_playable_card = True
    
    show_top_card()

    if player_has_playable_card:
        if len(player.cards) == 1:
            game_status = "ended"
            break
        else:
            show_current_player_cards()
            player_wants_to_play_card = input("Moechtest du eine Karte legen? (j/n): ")

            if player_wants_to_play_card == "j":
                player_chose_valid_card = False
                while not player_chose_valid_card:
                    gelegte_karte = input("Welche Karte moechtest du legen? (Zahl)")
                    zu_legende_karte = current_player.cards[gelegte_karte-1]
                    if top_card.can_card_be_put_on_top(zu_legende_karte):
                        player_chose_valid_card = True
                        top_card = zu_legende_karte
                        del current_player.cards[gelegte_karte-1]
                        
                        print("Karte", top_card.value, top_card.color, " wurde abgelegt")
                        print("Naechster Spieler ist an der Reihe")
                        input()
                    else:
                        print("Diese Karte kann nicht abgelegt werden")
    else:
        print("Du besitzt keine spielbaren Karten")
        input()
    

    current_player_count += 1
    cls()

winning_player = players[current_player_count-1]
print("Mau Mau fuer Spieler: ", player.name)

#Score Anzeigen

