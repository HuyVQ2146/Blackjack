"""
=============================================================
  BLACK JACK GAME  –  Troy University
  Giảng viên: Dr. Bernard Chen
  Sinh viên  : (Nhập tên của bạn)

  Cấu trúc theo slide bài giảng:
    1. Initiation  – khởi tạo biến, hàm, bộ bài
    2. Loop        – chia bài → người chơi → nhà cái → thắng/thua
=============================================================
"""

import random


# ─── 1. INITIATION ──────────────────────────────────────────

# 3 bộ bài (như yêu cầu slide 23)
SINGLE_DECK = (
    [1]*4 + [2]*4 + [3]*4 + [4]*4 + [5]*4 +
    [6]*4 + [7]*4 + [8]*4 + [9]*4 +
    [10]*4 + [11]*4 + [12]*4 + [13]*4
)

CARD_NAMES = {
    1:'A', 2:'2', 3:'3', 4:'4', 5:'5',
    6:'6', 7:'7', 8:'8', 9:'9',
    10:'10', 11:'J', 12:'Q', 13:'K'
}


def make_deck(num_decks=3):
    """Tạo bộ bài với num_decks bộ, xáo ngẫu nhiên."""
    deck = SINGLE_DECK * num_decks
    random.shuffle(deck)
    return deck


# ─── Hàm print_card (theo slide 9) ──────────────────────────
def print_card(x):
    """In hình ảnh ASCII của một lá bài (x là giá trị thô 1-13)."""
    label = CARD_NAMES[x]
    if len(label) == 1:          # 1 ký tự: A, 2..9, J, Q, K
        print("+---------+")
        print(f"| {label}       |")
        print("|         |")
        print("|         |")
        print(f"|       {label} |")
        print("+---------+")
    else:                        # 2 ký tự: "10"
        print("+---------+")
        print(f"| {label}      |")
        print("|         |")
        print("|         |")
        print(f"|      {label} |")
        print("+---------+")


def print_cards_side_by_side(card_list):
    """In nhiều lá bài trên cùng 1 hàng ngang cho đẹp."""
    rows = [[], [], [], [], [], []]
    for x in card_list:
        label = CARD_NAMES[x]
        pad = label.ljust(2)
        rows[0].append("+---------+")
        rows[1].append(f"| {pad}      |")
        rows[2].append("|         |")
        rows[3].append("|         |")
        rows[4].append(f"|      {pad} |")
        rows[5].append("+---------+")
    for row in rows:
        print("  ".join(row))


# ─── Hàm card_add (theo slide 10) ───────────────────────────
def card_add(total, x):
    """
    Cộng điểm lá bài vào tổng.
    Số 1-9 → đúng giá trị.
    10, J(11), Q(12), K(13) → cộng 10.
    Ace (1) tính là 1 để đơn giản (theo slide 8).
    """
    if x < 10:
        total += x
    else:
        total += 10
    return total


# ─── 2. VÒNG CHƠI CHÍNH ─────────────────────────────────────

def player_turn(player_id, deck):
    """Xử lý lượt của 1 người chơi. Trả về (tổng điểm, bust?)."""
    print(f"\n{'='*45}")
    print(f"  🙋  Lượt NGƯỜI CHƠI {player_id}")
    print(f"{'='*45}")

    player_sum = 0

    # Chia 2 lá đầu (slide 13)
    c1 = deck.pop()
    c2 = deck.pop()
    player_sum = card_add(player_sum, c1)
    player_sum = card_add(player_sum, c2)

    print(f"\n  Bài của bạn (Người chơi {player_id}):")
    print_cards_side_by_side([c1, c2])
    print(f"  📊 Tổng điểm: {player_sum}")

    # Kiểm tra Blackjack ngay
    if player_sum == 21:
        print("  🎉 BLACKJACK ngay lập tức!")
        return player_sum, False

    # Hỏi người chơi có muốn rút thêm không (slide 15)
    while True:
        try:
            choice = int(input("\n  Bạn có muốn rút thêm bài? (1: Có  /  0: Không): "))
        except ValueError:
            print("  ⚠️  Vui lòng nhập 1 hoặc 0.")
            continue

        if choice not in (0, 1):
            print("  ⚠️  Vui lòng nhập 1 hoặc 0.")
            continue

        if choice == 0:
            break

        # Rút thêm 1 lá
        c_new = deck.pop()
        player_sum = card_add(player_sum, c_new)
        print(f"\n  Lá bài mới:")
        print_cards_side_by_side([c_new])
        print(f"  📊 Tổng điểm: {player_sum}")

        if player_sum > 21:
            print(f"  💥  Bạn BUST! Quá 21 điểm.")
            return player_sum, True

        if player_sum == 21:
            print("  🎯 Đúng 21! Tuyệt vời!")
            break

    return player_sum, False


def house_turn(deck, player_sums):
    """
    Lượt của nhà cái (slide 17-20).
    - Nếu tất cả người chơi đều bust → nhà cái không cần chơi.
    - Nhà cái tự rút đến khi đánh bại ít nhất 1 người chơi hoặc bust.
    """
    print(f"\n{'='*45}")
    print("  🏦  Lượt HOUSE (Nhà Cái)")
    print(f"{'='*45}")

    active_sums = [s for s in player_sums if s <= 21]

    if not active_sums:
        print("  Tất cả người chơi đều Bust → House thắng tự động, không cần rút bài.")
        return None   # None = không cần so sánh

    max_player = max(active_sums)

    house_sum = 0
    c1 = deck.pop()
    c2 = deck.pop()
    house_sum = card_add(house_sum, c1)
    house_sum = card_add(house_sum, c2)

    print(f"\n  Bài của House:")
    print_cards_side_by_side([c1, c2])
    print(f"  📊 House tổng: {house_sum}")

    # House tự rút cho đến khi đạt hoặc vượt điểm cao nhất của người chơi (slide 20)
    while house_sum < max_player:
        print("\n  House tiếp tục rút...")
        c_new = deck.pop()
        house_sum = card_add(house_sum, c_new)
        print_cards_side_by_side([c_new])
        print(f"  📊 House tổng: {house_sum}")

        if house_sum > 21:
            print("  💥  House BUST! Quá 21 điểm.")
            return house_sum

    return house_sum


def judge(num_players, player_sums, player_busts, house_sum, chip_ins, money_list):
    """Phán xét thắng/thua và cập nhật tiền (slide 22)."""
    print(f"\n{'='*45}")
    print("  🏆  KẾT QUẢ VÁN NÀY")
    print(f"{'='*45}")

    winners = 0

    for i in range(num_players):
        ps = player_sums[i]
        chip = chip_ins[i]

        print(f"\n  Người chơi {i+1}:  Điểm = {ps}  |  House = {house_sum if house_sum is not None else 'N/A'}")

        if player_busts[i]:
            print(f"  ❌  Người chơi {i+1} BUST → THUA ${chip}")
            money_list[i] -= chip

        elif house_sum is None or house_sum > 21:
            # House bust → tất cả người chơi còn lại thắng
            print(f"  ✅  House Bust → Người chơi {i+1} THẮNG ${chip}!")
            money_list[i] += chip
            winners += 1

        elif ps == 21 and house_sum != 21:
            print(f"  🎉  21 điểm → Người chơi {i+1} THẮNG ${chip * 2}! (Blackjack bonus)")
            money_list[i] += chip * 2
            winners += 1

        elif ps > house_sum:
            print(f"  ✅  {ps} > {house_sum} → Người chơi {i+1} THẮNG ${chip}!")
            money_list[i] += chip
            winners += 1

        elif ps < house_sum:
            print(f"  ❌  {ps} < {house_sum} → Người chơi {i+1} THUA ${chip}")
            money_list[i] -= chip

        else:
            print(f"  🤝  Hòa! ({ps} = {house_sum}) → Hoàn lại cược.")

        print(f"       💰 Số dư: ${money_list[i]}")

    print(f"\n  Số người thắng ván này: {winners}/{num_players}")
    return money_list


# ─── MAIN ───────────────────────────────────────────────────
def main():
    print("\n" + "=" * 50)
    print("  🃏  WELCOME TO BLACK JACK TABLE!!  🃏")
    print("     Troy University – Dr. Bernard Chen")
    print("=" * 50)

    # Nhập số người chơi
    while True:
        try:
            num_players = int(input("\n  How many players? "))
            if 1 <= num_players <= 7:
                break
            print("  ⚠️  Từ 1 đến 7 người chơi.")
        except ValueError:
            print("  ⚠️  Nhập số nguyên hợp lệ.")

    # Nhập số tiền ban đầu cho mỗi người
    money_list = []
    for i in range(num_players):
        while True:
            try:
                m = int(input(f"  Người chơi {i+1} – Số tiền ban đầu: $"))
                if m > 0:
                    money_list.append(m)
                    break
                print("  ⚠️  Phải lớn hơn 0.")
            except ValueError:
                print("  ⚠️  Nhập số nguyên.")

    round_num = 0

    # ─── VÒNG LẶP CHÍNH ─────────────────────────────────────
    while True:
        # Kiểm tra còn ai chơi được không
        active = [i for i in range(num_players) if money_list[i] > 0]
        if not active:
            print("\n  💸  Tất cả người chơi đã hết tiền. Game Over!")
            break

        round_num += 1
        print(f"\n\n{'#'*50}")
        print(f"  VÁN #{round_num}")
        print(f"{'#'*50}")

        # Tạo bộ bài mới (3 decks theo slide 23)
        deck = make_deck(num_decks=3)

        # Đặt cược
        chip_ins = []
        for i in range(num_players):
            if money_list[i] <= 0:
                chip_ins.append(0)
                continue
            print(f"\n  Người chơi {i+1} – Số dư: ${money_list[i]}")
            while True:
                try:
                    chip = int(input(f"  Đặt cược: $"))
                    if 1 <= chip <= money_list[i]:
                        chip_ins.append(chip)
                        break
                    print(f"  ⚠️  Từ $1 đến ${money_list[i]}.")
                except ValueError:
                    print("  ⚠️  Nhập số nguyên.")

        # Lượt từng người chơi
        player_sums  = []
        player_busts = []

        for i in range(num_players):
            if chip_ins[i] == 0:
                player_sums.append(0)
                player_busts.append(True)
                continue
            ps, bust = player_turn(i + 1, deck)
            player_sums.append(ps)
            player_busts.append(bust)

        # Lượt nhà cái
        house_sum = house_turn(deck, player_sums)

        # Phán xét
        money_list = judge(num_players, player_sums, player_busts,
                           house_sum, chip_ins, money_list)

        # Tiếp tục?
        print()
        again = input("  Chơi ván tiếp theo? (1: Có  /  0: Không): ").strip()
        if again != '1':
            break

    # ─── TỔNG KẾT ───────────────────────────────────────────
    print("\n" + "=" * 50)
    print("  🎲  TỔNG KẾT GAME")
    print("=" * 50)
    print(f"  Tổng số ván đã chơi: {round_num}")
    for i in range(num_players):
        print(f"  Người chơi {i+1}: ${money_list[i]}")
    print("\n  Cảm ơn đã chơi! – Troy University 🎓")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
