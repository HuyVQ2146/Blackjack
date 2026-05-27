from collections import defaultdict
import time
from card_functions import (
    make_deck, add_value, display_total,
    print_card, print_cards_side_by_side
)

def get_int_input(prompt, min_val, max_val):
    """Prompt user for an integer within [min_val, max_val]. Repeats until valid."""
    check_set = {str(i) for i in range(min_val, max_val + 1)}
    value = input(prompt)
    while value not in check_set:
        value = input(f"Invalid input. Please enter a number between {min_val} and {max_val}: ")
    return int(value)


def play_again():
    """Ask if players want another round. Returns True/False."""
    restart = input("\n* Do you want to play again (1: yes, 0: no)? ")
    while restart != "1" and restart != "0":
        restart = input("Invalid choice. Please enter 1 to play again or 0 to quit: ")
    return restart == "1"


def deal_initial_hands(deck, num_players):
    """Deal 2 cards each to all players and the dealer.

    Returns:
        player_cards, player_total, player_ace_check,
        dealer_cards, dealer_total, dealer_ace_check, dealer_blackjack
    """
    player_cards = defaultdict(list)
    player_total = defaultdict(int)
    player_ace_check = defaultdict(int)

    for i in range(1, num_players + 1):
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
    dealer_cards = [deck.pop(), deck.pop()]
    dealer_total = 0
    dealer_ace_check = 0

    for card in dealer_cards:
        dealer_total, dealer_ace_check = add_value(
            dealer_total, card[0], dealer_ace_check
        )

    dealer_display = display_total(dealer_total, dealer_ace_check)
    dealer_blackjack = "Blackjack" in dealer_display
    if dealer_blackjack:
        print_cards_side_by_side(dealer_cards)
        print(f"Dealer has {dealer_display}! Dealer wins.")
        time.sleep(2)
    else:
        print_cards_side_by_side([dealer_cards[0], (0, " ")])
        hidden_val = min(dealer_cards[-1][0], 10)
        visible_total = dealer_total - hidden_val
        if dealer_cards[0][0] == 1:
            print(f"Dealer current points: {visible_total} or {visible_total + 10}\n\n")
        else:
            print(f"Dealer current points: {visible_total}\n\n")

    return (player_cards, player_total, player_ace_check,
            dealer_cards, dealer_total, dealer_ace_check, dealer_blackjack)


def player_turn(player_id, deck, cards, total, ace_check):
    """Run a single player's turn (hit/stand loop).

    Returns:
        (new_total, new_ace_check, bust)
    """
    print(f"Player {player_id}'s turn:\n")
    time.sleep(2)

    print(f"Player {player_id} cards:")
    print_cards_side_by_side(cards)
    print(f"Player {player_id} current points: "
          f"{display_total(total, ace_check)}")

    while total < 21:
        check_choice = input("\nDo you want to hit or stand? (1: hit, 0: stand): ")
        while check_choice != "1" and check_choice != "0":
            check_choice = input("Invalid choice. Please enter 1 to hit or 0 to stand: ")
        choice = int(check_choice)
        print()

        if choice == 1:
            new_card = deck.pop()
            cards.append(new_card)
            total, ace_check = add_value(total, new_card[0], ace_check)

            time.sleep(2)
            print("You drew:")
            print_card(new_card[0], new_card[1])
            time.sleep(2)

            print("Your current cards:")
            print_cards_side_by_side(cards)
            print(f"Your current points: {display_total(total, ace_check)}")

            if total == 21:
                print("\n\nBlackjack! You win.")
                time.sleep(2)
                return total, ace_check, False
            elif total > 21:
                print("\n\nBust! You lose.\n")
                time.sleep(2)
                return total, ace_check, True

        elif choice == 0:
            return total, ace_check, False

        time.sleep(2)

    return total, ace_check, False


def dealer_turn(deck, dealer_cards, dealer_total, dealer_ace_check):
    """Run the dealer's turn (hit until >= 17).

    Returns:
        (new_total, new_ace_check)
    """
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

    return dealer_total, dealer_ace_check


def settle_results(player_total, player_ace_check,
                   dealer_total, dealer_ace_check, num_players):
    """Compare all players vs dealer and print results."""
    time.sleep(2)
    print("\n=============== Game Result ===============")
    time.sleep(2)

    for i in range(1, num_players + 1):
        print(f"Player {i} total points: "
              f"{display_total(player_total[i], player_ace_check[i])}")
    print(f"Dealer total points: "
          f"{display_total(dealer_total, dealer_ace_check)}")
    time.sleep(1)

    print()
    if dealer_total > 21:
        print("Dealer busts!")
        for i in range(1, num_players + 1):
            if player_total[i] > 21:
                print(f"Player {i} busts and loses.")
            else:
                print(f"Player {i} wins.")
    else:
        for i in range(1, num_players + 1):
            if player_total[i] > 21:
                print(f"Player {i} busts and loses.")
            elif player_total[i] > dealer_total:
                print(f"Player {i} wins.")
            elif player_total[i] == dealer_total:
                print(f"Player {i} ties with the dealer.")
            else:
                print(f"Player {i} loses.")
