cards = input().split()
shuffles_count = int(input())
middle_length = len(cards) // 2

new_deck = []

for _ in range(shuffles_count):
    for index in range(middle_length):
        first_card = cards[index]
        index_second_part = index + middle_length
        second_card = cards[index_second_part]
        new_deck.append(first_card)
        new_deck.append(second_card)
    cards = new_deck
    new_deck = []

print(cards)
