import random
cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    card = random.choice(cards)
    return card

def get_total(hand):
    total = sum(hand)
    # turns the ace into a 1 if necessary
    if total > 21 and 11 in hand:
        total -= 10
    return total

player_hand = []
dealer_hand = []

player_hand.append(draw_card())
player_hand.append(draw_card())
dealer_hand.append(draw_card())
dealer_hand.append(draw_card())

print("Welcome to Blackjack!")
player_hit = "y"
while player_hit == "y":
    player_total = get_total(player_hand)

    if player_total > 21:
        break
    print(f"Player hand: {player_hand}, total is {player_total}")
    print(f"Dealer hand: {dealer_hand[0]} with one card hidden.")

    player_hit = input("Would you like to hit? y/n: ").lower()
    if player_hit == "n":
        break

    player_hand.append(draw_card())


dealer_total = get_total(dealer_hand)
while dealer_total < 17:
    dealer_hand.append(draw_card())
    dealer_total = get_total(dealer_hand)

print(f"Player hand: {player_hand}, total is {player_total}")
print(f"Dealer hand: {dealer_hand}, total is {dealer_total}.")

if player_total > 21:
    print("Player busts!")
elif dealer_total > 21:
    print("Dealer busts")
elif player_total > dealer_total and player_total < 22:
    print("Player wins!")
elif player_total < dealer_total:
    print("Player loses!")
elif player_total == dealer_total:
    print("Draw!")
else: 
    print("Player loses!")