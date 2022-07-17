card_sum = 0
for _ in range(5):
    card = input()
    if card.isdecimal():
        card_sum += int(card)
    if 'A' in card:
        card_sum += 1
    if 'K' in card:
        card_sum += 13
    if 'Q' in card:
        card_sum += 12
    if 'J' in card:
        card_sum += 11
print(card_sum)
