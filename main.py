import time
from collections import defaultdict
from card_functions import (
    make_deck, add_value, display_total,
    print_card, print_cards_side_by_side
)


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
        player_ace_check = defaultdict(int)

        game = True
        time.sleep(2)

        for i in range(1, count_people + 1):
            print(f"\n\nPlayer {i} cards:")
            for _ in range(2):
                card = deck.pop()
                player_cards[i].append(card)
                player_total[i], player_ace_check[i] = add_value(
                    player_total[i], card[0], player_ace_check[i]
                )
            print_cards_side_by_side(player_cards[i])
            print(f"Player {i} total points: "
                  f"{display_total(player_total[i], player_ace_check[i])}")
            time.sleep(2)

        print("\n\nDealer's cards:")
        dealer_cards = [deck.pop() for _ in range(2)]
        dealer_total = 0
        dealer_card_list = []
        dealer_ace_check = 0

        for card in dealer_cards:
            dealer_card_list.append(card)
            dealer_total, dealer_ace_check = add_value(
                dealer_total, card[0], dealer_ace_check
            )

        dealer_display = display_total(dealer_total, dealer_ace_check)
        if "Blackjack" in dealer_display:
            print_cards_side_by_side(dealer_card_list)
            print(f"Dealer has {dealer_display}! Dealer wins.")
            game = False
            time.sleep(2)
        else:
            print_cards_side_by_side([dealer_card_list[0], (0, " ")])
            hidden_val = min(dealer_card_list[-1][0], 10)
            visible_total = dealer_total - hidden_val
            if dealer_card_list[0][0] == 1:
                print(f"Dealer current points: {visible_total} or {visible_total + 10}\n\n")
            else:
                print(f"Dealer current points: {visible_total}\n\n")

        while game:
            time.sleep(2)
            print("===========================================")
            for i in range(1, count_people + 1):
                print(f"Player {i}'s turn:\n")
                time.sleep(2)

                print(f"Player {i} cards:")
                print_cards_side_by_side(player_cards[i])
                print(f"Player {i} current points: "
                      f"{display_total(player_total[i], player_ace_check[i])}")

                while player_total[i] < 21:
                    check_choice = input("\nDo you want to hit or stand? (1: hit, 0: stand): ")
                    while check_choice != "1" and check_choice != "0":
                        check_choice = input("Invalid choice. Please enter 1 to hit or 0 to stand: ")
                    choice = int(check_choice)
                    print()

                    if choice == 1:
                        new_card = deck.pop()
                        player_cards[i].append(new_card)
                        player_total[i], player_ace_check[i] = add_value(
                            player_total[i], new_card[0], player_ace_check[i]
                        )

                        time.sleep(2)
                        print("You drew:")
                        print_card(new_card[0], new_card[1])
                        time.sleep(2)

                        print("Your current cards:")
                        print_cards_side_by_side(player_cards[i])
                        print(f"Your current points: "
                              f"{display_total(player_total[i], player_ace_check[i])}")

                        if player_total[i] == 21:
                            print("\n\nBlackjack! You win.")
                            time.sleep(2)
                            break
                        elif player_total[i] > 21:
                            print("\n\nBust! You lose.\n")
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
            print(f"Dealer total points: "
                  f"{display_total(dealer_total, dealer_ace_check)}")

            while dealer_total < 17:
                time.sleep(2)
                new_card = deck.pop()
                dealer_cards.append(new_card)
                dealer_total, dealer_ace_check = add_value(
                    dealer_total, new_card[0], dealer_ace_check
                )

                print("\nDealer drew:")
                print_card(new_card[0], new_card[1])
                time.sleep(2)

                print("Dealer's current cards:")
                print_cards_side_by_side(dealer_cards)
                print(f"Dealer total points: "
                      f"{display_total(dealer_total, dealer_ace_check)}")

                if dealer_total > 21:
                    print("\nDealer bust!\n\n")
                    break
                elif dealer_total >= 17:
                    print("\nDealer stands.\n\n")
            break

        time.sleep(2)

        print("=============== Game Result ===============")
        time.sleep(2)
        for i in range(1, count_people + 1):
            print(f"Player {i} total points: "
                  f"{display_total(player_total[i], player_ace_check[i])}")
        print(f"Dealer total points: "
              f"{display_total(dealer_total, dealer_ace_check)}")
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
                elif player_total[i] > dealer_total:
                    print(f"Player {i} wins.")
                elif player_total[i] == dealer_total:
                    print(f"Player {i} ties with the dealer.")
                else:
                    print(f"Player {i} loses.")

        restart = input("\n* Do you want to play again (1: yes, 0: no)? ")
        while restart != "1" and restart != "0":
            restart = input("Invalid choice. Please enter 1 to play again or 0 to quit: ")
        if restart == '1':
            time.sleep(2)
        else:
            Continue = False

    print("\n*** Thanks for playing! Goodbye! ***")


if __name__ == "__main__":
    main()
