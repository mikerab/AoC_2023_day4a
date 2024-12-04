import time

doc = open("input.txt", "rt")

original_cards = []
copied_cards = []

start_time = time.time()

for line in doc:
    line = " ".join(line.split())
    # print(line)
    card_name = line.split(":")
    original_cards.append(card_name[0])
    # print(card_name)
    all_numbers = card_name[1]
    # print(all_numbers)
    temp = all_numbers.split("|")
    winning_numbers = temp[0].strip().split(" ")
    card_numbers = temp[1].strip().split(" ")

    numbers_won = []
    card_copies = 0

    for num in card_numbers:
        if num in winning_numbers:
            numbers_won.append(num)
            card_copies = card_copies + 1


    # print(f"{card_name[0]} has {len(numbers_won)} match(es): {numbers_won} and gets {card_copies} additional cards.")

    # award additional cards from the original card
    temp = card_name[0].split(" ")
    orig_card_number = int(temp[1])
    count_of_copies = copied_cards.count(card_name[0])
    for outer in range(1, 2 + count_of_copies):
        for i in range(orig_card_number + 1, orig_card_number + 1 + card_copies):
            copied_cards.append("Card " + str(i))

# print(f"The original list of cards is {original_cards}")
# print(f"The copied list of cards is {copied_cards}")

elapsed_time = time.time() - start_time
print(f"The total number of cards is {len(original_cards) + len(copied_cards)} (Elapsed Time: {elapsed_time})")


doc.close()
