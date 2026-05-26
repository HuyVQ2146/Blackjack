import random

SINGLE_DECK = [
    (1,"♠"), (2,"♠"), (3,"♠"), (4,"♠"), (5,"♠"), (6,"♠"), (7,"♠"), (8,"♠"), (9,"♠"), (10,"♠"), (11,"♠"), (12,"♠"), (13,"♠"),
    (1,"♣"), (2,"♣"), (3,"♣"), (4,"♣"), (5,"♣"), (6,"♣"), (7,"♣"), (8,"♣"), (9,"♣"), (10,"♣"), (11,"♣"), (12,"♣"), (13,"♣"),
    (1,"♦"), (2,"♦"), (3,"♦"), (4,"♦"), (5,"♦"), (6,"♦"), (7,"♦"), (8,"♦"), (9,"♦"), (10,"♦"), (11,"♦"), (12,"♦"), (13,"♦"),
    (1,"♥"), (2,"♥"), (3,"♥"), (4,"♥"), (5,"♥"), (6,"♥"), (7,"♥"), (8,"♥"), (9,"♥"), (10,"♥"), (11,"♥"), (12,"♥"), (13,"♥")
]

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

def print_card(x, Type):
    label = CARD_NAMES[x]
    if x != 10:
        print("+---------+")
        print(f"| {label}       |")
        print("|         |")
        print(f"|    {Type}    |")
        print("|         |")
        print(f"|       {label} |")
        print("+---------+\n")
    else:
        print("+---------+")
        print(f"| {label}      |")
        print("|         |")
        print(f"|    {Type}    |")
        print("|         |")
        print(f"|      {label} |")
        print("+---------+\n")

def print_cards_side_by_side(card_list):
    rows = [[], [], [], [], [], [], []]
    for x, Type in card_list:
        label = CARD_NAMES[x]
        if x == 0:
            rows[0].append("+---------+")
            rows[1].append("|         |")
            rows[2].append("|         |")
            rows[3].append("|         |")
            rows[4].append("|         |")
            rows[5].append("|         |")
            rows[6].append("+---------+")
        elif x != 10:
            rows[0].append("+---------+")
            rows[1].append(f"| {label}       |")
            rows[2].append("|         |")
            rows[3].append(f"|    {Type}    |")
            rows[4].append("|         |")
            rows[5].append(f"|       {label} |")
            rows[6].append("+---------+")
        else:
            rows[0].append("+---------+")
            rows[1].append(f"| {label}      |")
            rows[2].append("|         |")
            rows[3].append(f"|    {Type}    |")
            rows[4].append("|         |")
            rows[5].append(f"|      {label} |")
            rows[6].append("+---------+")
    for row in rows:
        print("   ".join(row))
    print()

def add_value(total: int, card_value: int, ace_check_plus: int) -> tuple[int, int]:
    """
    Update hand total when a new card is added.

    On each card draw:
    - Ace adds 11 and sets ace_check_plus = 1 (hand now has an ace).
    - Number cards 2-9 add face value.
    - Face cards (10-K) add 10.

    If total exceeds 21 and an ace is currently counted as 11
    (ace_check_plus == 1), the ace is downgraded: total -= 10,
    ace_check_plus = 0. The while loop handles multiple downgrades
    across sequential calls (e.g., drawing a third ace after two
    aces already downgraded one).

    ace_check_plus meaning:
    - 0: no ace in hand, OR ace was downgraded (total has no +10)
    - 1: an ace is currently counted as 11 in the total

    Returns
    -------
    tuple[int, int]
        (updated total, ace_check_plus).
    """
    if card_value == 1:
        total += 11
        ace_check_plus = 1
    elif card_value < 10:
        total += card_value
    else:
        total += 10

    if total > 21 and ace_check_plus == 1:
        total -= 10
        ace_check_plus = 0

    return total, ace_check_plus

def display_total(total: int, ace_check_plus: int) -> str:
    """
    Return a display string for the hand.

    When ace_check_plus == 1, the total includes one ace as 11.
    The hard value (that ace as 1 instead) is total - 10.

    Examples:
        total=16, ace_check_plus=1  -> "6 or 16"   (soft 16)
        total=21, ace_check_plus=1  -> "21 (Blackjack)"
        total=12, ace_check_plus=0  -> "12"         (hard, no ace as 11)
    """
    if ace_check_plus == 1:
        hard = total - 10
        if total == 21:
            return f"{total} (Blackjack)"
        return f"{hard} or {total}"
    return str(total)
