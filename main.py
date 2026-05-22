import random
from collections import defaultdict

SINGLE_DECK = (
    [1]*4 + [2]*4 + [3]*4 + [4]*4 + [5]*4 +
    [6]*4 + [7]*4 + [8]*4 + [9]*4 +
    [10]*4 + [11]*4 + [12]*4 + [13]*4
)

CARD_NAMES = {
    0:' ',
    1:'A', 2:'2', 3:'3', 4:'4', 5:'5',
    6:'6', 7:'7', 8:'8', 9:'9',
    10:'10', 11:'J', 12:'Q', 13:'K'
}

def make_deck(num_decks=3):
    deck = SINGLE_DECK * num_decks
    random.shuffle(deck)
    return deck

def print_card(x):
    if x != 10:
        label = CARD_NAMES[x]
        print("+---------+")
        print(f"| {label}       |")
        print("|         |")
        print("|         |")
        print(f"|       {label} |")
        print("+---------+\n")
    else:
        label = CARD_NAMES[x]
        print("+---------+")
        print(f"| {label}      |")
        print("|         |")
        print("|         |")
        print(f"|      {label} |")
        print("+---------+\n")
    

def add_value(total, x):
    if x < 10:
        total += x
    else:
        total += 10
    return total



# The game
Continue = True
while Continue:
    print("\n\n\n===========================================\n")
    print("========== Welcome to Blackjack! ==========\n")
    print("===========================================\n")
    
    deck = make_deck(int(input("Choose the number of decks: ")))
    count_people = int(input("Enter number of players: "))

    print("\n=============== Set Game ===============")
    player_cards = defaultdict(list)
    player_total = defaultdict(int)
    for i in range(1, count_people + 1):
        print(f"Player {i} cards:")
        for _ in range(2):
            card = deck.pop()
            player_cards[i].append(card)
            player_total[i] = add_value(player_total[i], card)
            print_card(card)
        print(f"Player {i} total points: {player_total[i]}\n\n")

    print("Dealer's cards:")
    dealer_cards = [deck.pop()]
    dealer_total = 0
    for card in dealer_cards:
        dealer_total = add_value(dealer_total, card)
        print_card(card)
    print_card(0)
    print(f"Dealer current points: {dealer_total}\n\n")

    while True:
        print("===========================================")
        for i in range(1, count_people + 1):
            print(f"Player {i}'s turn:")
            
            while player_total[i] < 21:
                print(f"\nPlayer {i} current total points: {player_total[i]}")
                print("Do you want to hit or stand? (1: hit, 0: stand)")
                choice = int(input())
                while choice != 1 and choice != 0:
                    print("Invalid choice. Please enter 1 to hit or 0 to stand.")
                if choice == 1:
                    new_card = deck.pop()
                    player_cards[i].append(new_card)
                    player_total[i] = add_value(player_total[i], new_card)
                    print("You drew:")
                    print_card(new_card)
                    print(f"Player {i} total points: {player_total[i]}")
                    
                    if player_total[i] == 21:
                        print("Blackjack! You win.")
                        break
                    
                    if player_total[i] > 21:
                        print("Bust! You lose.")
                        
                elif choice == 0:
                    if i == count_people:
                        print("You stand. Dealer's turn.\n")
                    else:    
                        print("You stand. Next player's turn.\n")
                    break
            print("\n===========================================")
                
        while dealer_total < 17:
            new_card = deck.pop()
            dealer_cards.append(new_card)
            dealer_total = add_value(dealer_total, new_card)
            print("Dealer drew:")
            print_card(new_card)
            print(f"Dealer total points: {dealer_total}")
            if dealer_total > 21:
                print("Dealer bust!")
            if dealer_total >= 17:
                print("Dealer stands.\n\n")
        break
        
            
    print("=============== Game Result ===============")
    for i in range(1, count_people + 1):
        print(f"Player {i} total points: {player_total[i]}")
    print(f"Dealer total points: {dealer_total}\n")

    if dealer_total > 21:
        print("Dealer busts!")
        for i in range(1, count_people + 1):
            if player_total[i] > 21:
                print(f"Player {i} busts and loses.")
            else:
                print(f"Player {i} wins.")
    else:
        for i in range(1, count_people + 1):
            if player_total[i] > 21:
                print(f"Player {i} busts and loses.")
            elif player_total[i] > dealer_total:
                print(f"Player {i} wins.")
            elif player_total[i] < dealer_total:
                print(f"Player {i} loses.")
            else:
                print(f"Player {i} ties with the dealer.")
    restart = input("\n\n* Do you want to play again(1: yes, 0: no) ? ")
    if restart == '1':
        Continue = True
    else:
        Continue = False
print("*** Thanks for playing! Goodbye! ***")
