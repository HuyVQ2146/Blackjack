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
        
        check_num_people = input("Enter number of players (1-7): ")
        check_num_people = {"1", "2", "3", "4", "5", "6", "7"}
        while check_num_people not in check_num_people:
            check_num_people = input("Invalid input. Please enter a number between 1 and 7: ")
        count_people = int(check_num_people)
        print()

        print("\n================ Set Game =================")
        player_cards = defaultdict(list)
        player_total = defaultdict(int)
        
        time.sleep(2)
        
        for i in range(1, count_people + 1):
            print(f"Player {i} cards:")
            for _ in range(2):
                card = deck.pop()
                player_cards[i].append(card)
                player_total[i] = add_value(player_total[i], card[0])
            print_cards_side_by_side(player_cards[i])
            print(f"Player {i} total points: {player_total[i]}\n\n")
            time.sleep(2)
            
        

        print("Dealer's cards:")
        dealer_cards = [deck.pop() for _ in range(2)]
        dealer_total = 0
        dealer_card_list = []
        
        for card in dealer_cards:
            dealer_total = add_value(dealer_total, card[0])
            dealer_card_list.append(card)   
        
        if dealer_total == 21:
            print_cards_side_by_side(dealer_card_list)
            print("Dealer has Blackjack! Dealer wins.")
            time.sleep(2)
        else: 
            print_cards_side_by_side([dealer_card_list[0], (0, " ")])
            print(f"Dealer current points: {dealer_total - min(dealer_card_list[-1][0], 10)}\n\n")
         
        time.sleep(2)
        

        while True:
            print("===========================================")
            for i in range(1, count_people + 1):
                print(f"Player {i}'s turn:\n")
                
                time.sleep(2)
                
                print(f"Player {i} cards:")
                print_cards_side_by_side(player_cards[i])
                print(f"Player {i} current total points: {player_total[i]}\n")
                
                while player_total[i] < 21:
                    check_choice = input("Do you want to hit or stand? (1: hit, 0: stand): ")
                    while check_choice != "1" and check_choice != "0":
                        check_choice = input("Invalid choice. Please enter 1 to hit or 0 to stand: ")
                    choice = int(check_choice)
                    print()
                    
                    if choice == 1:
                        new_card = deck.pop()
                        player_cards[i].append(new_card)
                        player_total[i] = add_value(player_total[i], new_card[0])
                        
                        time.sleep(2)
                        
                        print("You drew:")
                        print_card(new_card[0], new_card[1])
                        
                        time.sleep(2)
                        
                        print("Your current cards:")
                        print_cards_side_by_side(player_cards[i])
                        print(f"Player {i} total points: {player_total[i]}\n")
                        
                        if player_total[i] == 21:
                            print("Blackjack! You wins.")
                            time.sleep(2)
                            break
                        elif player_total[i] > 21:
                            print("Bust! You loses.")
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
            print(f"Dealer current points: {dealer_total}\n")
            while dealer_total < 17:
                time.sleep(2)
                
                new_card = deck.pop()
                dealer_cards.append(new_card)
                dealer_total = add_value(dealer_total, new_card[0])
                print("Dealer drew:")
                print_card(new_card[0], new_card[1])
                
                time.sleep(2)
                
                print("Dealer's current cards:")
                print_cards_side_by_side(dealer_cards)
                print(f"Dealer total points: {dealer_total}\n")
                if dealer_total > 21:
                    print("Dealer bust!\n\n")
                elif dealer_total >= 17:
                    print("Dealer stands.\n\n")
            time.sleep(2)
            break
            
                
        print("=============== Game Result ===============")
        time.sleep(2)
        for i in range(1, count_people + 1):
            print(f"Player {i} total points: {player_total[i]}")
        print(f"Dealer total points: {dealer_total}\n")
        time.sleep(1)
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
            time.sleep(2)
        else:
            Continue = False
    print("*** Thanks for playing! Goodbye! ***")
    
if __name__ == "__main__":
    main()
    
