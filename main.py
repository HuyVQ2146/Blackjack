import time
from game_logic import *
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

        num_decks = get_int_input("Choose the number of decks (1-8): ", 1, 8)
        deck = make_deck(num_decks)
        print()

        num_players = get_int_input("Enter number of players (1-7): ", 1, 7)
        print()

        print("\n================ Set Game =================")
        time.sleep(2)

        (player_cards, player_total, player_ace_check,
         dealer_cards, dealer_total, dealer_ace_check,
         dealer_blackjack) = deal_initial_hands(deck, num_players)

        if dealer_blackjack:
            settle_results(player_total, player_ace_check,
                           dealer_total, dealer_ace_check, num_players)
            Continue = play_again()
            continue

        game = True
        player_busts = {}
        while game:
            time.sleep(2)
            print("===========================================")
            for i in range(1, num_players + 1):
                total, ace_check, bust = player_turn(
                    i, deck, player_cards[i], player_total[i], player_ace_check[i]
                )
                player_total[i] = total
                player_ace_check[i] = ace_check
                player_busts[i] = bust
                print("\n===========================================")

            dealer_total, dealer_ace_check = dealer_turn(
                deck, dealer_cards, dealer_total, dealer_ace_check
            )
            break

        settle_results(player_total, player_ace_check,
                       dealer_total, dealer_ace_check, num_players)

        Continue = play_again()

    print("\n*** Thanks for playing! Goodbye! ***")


if __name__ == "__main__":
    main()
