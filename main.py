import time
from collections import defaultdict
from card_functions import *

# The game
def main():
    Continue = True
    while Continue:
        print("\n\n\n===========================================\n")
        print("========== Welcome to Blackjack! ==========\n")
        print("===========================================\n")
        
        
        num_decks = input("Choose the number of decks (1-8): ")
        check_num_decks = {"1", "2", "3", "4", "5", "6", "7", "8"}
        while num_decks not in check_num_decks:
            num_decks = input("Invalid input. Please enter a number between 1 and 8: ")
        deck = make_deck(int(num_decks))
        print()
        
        num_people = input("Enter number of players (1-7): ")
        check_num_people = {"1", "2", "3", "4", "5", "6", "7"}
        while num_people not in check_num_people:
            num_people = input("Invalid input. Please enter a number between 1 and 7: ")
        count_people = int(num_people)
        print()

        print("\n================ Set Game =================")
        player_cards = defaultdict(list)
        player_total = defaultdict(int)
        Ace_alter_points = defaultdict(int)
        check_aces = defaultdict(bool)
        game = True
        
        time.sleep(2)
        
        for i in range(1, count_people + 1):
            print(f"\n\nPlayer {i} cards:")
            for _ in range(2):
                card = deck.pop()
                player_cards[i].append(card)
                player_total[i] = add_value(player_total[i], card[0])
                ace_handling(check_aces, Ace_alter_points, card, player_total, i) 
            print_cards_side_by_side(player_cards[i])
            print_points(i, check_aces, Ace_alter_points, player_total)
            time.sleep(2)
            
        

        print("\n\nDealer's cards:")
        dealer_cards = [deck.pop() for _ in range(2)]
        dealer_total = 0
        dealer_card_list = []
        
        # set index 0 in 'check_aces' and 'Ace_alter_points' for dealer
        for card in dealer_cards:
            dealer_card_list.append(card)   
            dealer_total = add_value(dealer_total, card[0])
            ace_handling(check_aces, Ace_alter_points, card, dealer_total, 0) 
        
        if Ace_alter_points[0] == 21:
            print_cards_side_by_side(dealer_card_list)
            print("Dealer has Blackjack! Dealer wins.")
            game = False
            time.sleep(2)
        else: 
            print_cards_side_by_side([dealer_card_list[0], (0, " ")])
            if dealer_card_list[0][0] == 1:
                print(f"Dealer current points: {dealer_total - min(dealer_card_list[-1][0], 10)} or {Ace_alter_points[0] - min(dealer_card_list[-1][0], 10)}\n\n")
            else:
                print(f"Dealer current points: {dealer_total - min(dealer_card_list[-1][0], 10)}\n\n")



        while game:
            time.sleep(2)
            print("===========================================")
            for i in range(1, count_people + 1):
                print(f"Player {i}'s turn:\n")
                
                time.sleep(2)
                
                print(f"Player {i} cards:")
                print_cards_side_by_side(player_cards[i])
                print(f"Player {i} current points: {player_total[i]}")
                
                while player_total[i] < 21 and Ace_alter_points[i] != 21:
                    check_choice = input("\nDo you want to hit or stand? (1: hit, 0: stand): ")
                    while check_choice != "1" and check_choice != "0":
                        check_choice = input("Invalid choice. Please enter 1 to hit or 0 to stand: ")
                    choice = int(check_choice)
                    print()
                    
                    if choice == 1:
                        new_card = deck.pop()
                        player_cards[i].append(new_card)
                        player_total[i] = add_value(player_total[i], new_card[0])
                        ace_handling(check_aces, Ace_alter_points, new_card, player_total, i)
                        
                        time.sleep(2)
                        
                        print("You drew:")
                        print_card(new_card[0], new_card[1])
                        
                        time.sleep(2)
                        
                        print("Your current cards:")
                        print_cards_side_by_side(player_cards[i])
                        print_points(i, check_aces, Ace_alter_points, player_total)
                        
                        if player_total[i] == 21 or Ace_alter_points[i] == 21:
                            print("\n\nBlackjack! You wins.")
                            time.sleep(2)
                            break
                        elif player_total[i] > 21:
                            print("\n\nBust! You loses.\n")
                            time.sleep(2)
                            break
                    elif choice == 0:
                        if i == count_people:
                            print(f"You stand. Dealer's turn.\n")
                        else:    
                            print(f"You stand. Next player's turn.\n")
                        time.sleep(2)
                        break
                    time.sleep(2)
                print("\n===========================================")
            
            print("Dealer's turn:\n")
            
            time.sleep(2)
            
            print("Dealer's cards:")
            print_cards_side_by_side(dealer_cards)
            print_points(0, check_aces, Ace_alter_points, dealer_total)
            
            
            while dealer_total < 17:
                time.sleep(2)
                
                new_card = deck.pop()
                dealer_cards.append(new_card)
                dealer_total = add_value(dealer_total, new_card[0])
                ace_handling(check_aces, Ace_alter_points, new_card, dealer_total, 0)
                print("\nDealer drew:")
                print_card(new_card[0], new_card[1])
                
                time.sleep(2)
                
                print("Dealer's current cards:")
                print_cards_side_by_side(dealer_cards)
                print_points(0, check_aces, Ace_alter_points, dealer_total)
                if dealer_total > 21:
                    print("\nDealer bust!\n\n")
                    break
                elif dealer_total >= 17:
                    print("\nDealer stands.\n\n")
            break
        time.sleep(2)       
        
        print("\n=============== Game Result ===============")
        time.sleep(2)
        for i in range(1, count_people + 1):
            print_points(i, check_aces, Ace_alter_points, player_total)
        print_points(0, check_aces, Ace_alter_points, dealer_total)
        time.sleep(1)
        
        print()
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
                elif (
                    (player_total[i] > dealer_total) or 
                    (check_aces[i] and Ace_alter_points[i] > dealer_total and Ace_alter_points[i] <= 21)
                ):
                    print(f"Player {i} wins.")
                elif player_total[i] == dealer_total or (check_aces[i] and Ace_alter_points[i] == dealer_total):
                    print(f"Player {i} ties with the dealer.")
                else:
                    print(f"Player {i} loses.")
        restart = input("\n* Do you want to play again(1: yes, 0: no) ? ")
        while restart != "1" and restart != "0":
            restart = input("Invalid choice. Please enter 1 to play again or 0 to quit: ")
        if restart == '1':
            time.sleep(2)
        else:
            Continue = False
    print("\n*** Thanks for playing! Goodbye! ***")
    
if __name__ == "__main__":
    main()
    
