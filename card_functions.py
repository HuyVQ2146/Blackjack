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

def add_value(total, x):
    if x < 10:
        total += x
    else:
        total += 10
    return total
