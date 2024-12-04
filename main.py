
# This is part one... part two will build on top.
doc = open("input.txt", "rt")

total_points = 0

for line in doc:
    line = " ".join(line.split())
    print(line)
    card_name = line.split(":")
    # print(card_name)
    all_numbers = card_name[1]
    # print(all_numbers)
    temp = all_numbers.split("|")
    winning_numbers = temp[0].strip().split(" ")
    card_numbers = temp[1].strip().split(" ")

    # print(f"winning numbers: {winning_numbers}")
    # print(f"my numbers: {card_numbers}")

    numbers_won = []
    card_points = 0

    for num in card_numbers:
        if num in winning_numbers:
            numbers_won.append(num)
            if card_points == 0:
                card_points = 1
            else:
                card_points = card_points * 2

    total_points = total_points + card_points

    print(f"{card_name[0]} has {len(numbers_won)} match(es): {numbers_won} and has {card_points} points.")

print(f"The pile of cards has {total_points} total points!!")


doc.close()
