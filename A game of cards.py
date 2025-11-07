import random

# Card values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'ace': 11
}

def create_deck():
    """Creates a standard 52-card deck."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = list(CARD_VALUES.keys())
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    """Deals a single card from the deck."""
    return deck.pop()

def calculate_hand_value(hand):
    """Calculates the value of a hand, handling Aces."""
    value = 0
    num_aces = 0
    for card_rank, _ in hand:
        value += CARD_VALUES[card_rank]
        if card_rank == 'A':
            num_aces += 1

    while value > 21 and num_aces > 0:
        value -= 10  # Change Ace value from 11 to 1
        num_aces -= 1
    return value

def display_hand(name, hand, hide_dealer_card=False):
    """Displays the cards in a hand."""
    print(f"{name}'s hand:")
    if hide_dealer_card and name == "Dealer":
        print(f"  [{hand[0][0]} of {hand[0][1]}] [Hidden Card]")
    else:
        for card_rank, card_suit in hand:
            print(f"  [{card_rank} of {card_suit}]")
    print(f"  Value: {calculate_hand_value(hand) if not (hide_dealer_card and name == 'Dealer') else '?'}\n")

def play_blackjack():
    """Main function to play a game of Blackjack."""
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Initial deal
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))

    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand, hide_dealer_card=True)

    # Player's turn
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value == 21:
            print("Blackjack! Player wins!")
            return
        if player_value > 21:
            print("Player busts! Dealer wins!")
            return

        action = input("Do you want to (H)it or (S)tand? ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
            display_hand("Player", player_hand)
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'H' or 'S'.")

    # Dealer's turn
    display_hand("Dealer", dealer_hand, hide_dealer_card=False) # Reveal dealer's hand
    while calculate_hand_value(dealer_hand) < 17:
        print("Dealer hits...")
        dealer_hand.append(deal_card(deck))
        display_hand("Dealer", dealer_hand, hide_dealer_card=False)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("Dealer busts! Player wins!")
    elif player_value > dealer_value:
        print("Player wins!")
    elif dealer_value > player_value:
        print("Dealer wins!")
    else:
        print("It's a push!")

if __name__ == "__main__":
    play_blackjack()