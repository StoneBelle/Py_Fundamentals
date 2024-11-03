import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(player):
    """Randomly draws a card from the array. Also checks and adjusts scores if player draws an Ace."""
    drawn = random.choice(cards)
    score = player

    # Checks if drawn card is an ace
    if drawn == 11:
        ace_adjustment = player + drawn
        
        # Adjust ace to value of "1" if adding "11" to a hand > 21
        if ace_adjustment > 21:
            score += 1
            print("Ace +1")
        
        else:
            score += drawn
            print("Ace +11")
    else:
        score += drawn
    
    # print(f"you drawn {drawn}, updated score {score}")
    return score


def check_cards(p1, p2):
    """Checks the final hand of both players to determine the winner."""
    if p1 > 21 and p2 >  21 or p1 == p2:
        print(f"It's a Draw! Player 1: {p1}, Player 2: {p2}")
        return False

    elif p1 > 21 and p2 <= 21:
        print(f"You Win! Player 1: {p1}, Player 2: {p2}")
        return False

    elif p1 <= 21 and p2 > 21:
        print(f"You Lose! Player 1: {p1}, Player 2: {p2}")
        return False
    
    elif p1 > p2:
        print(f"You Win! Player 1: {p1}, Player 2: {p2}")

    elif p1 < p2:
        print(f"You Lose! Player 1: {p1}, Player 2: {p2}")

    else:
        return True

# Ask use if they would like to play
play = input('Play a round of Blackjack? "Y" or "N": ').upper()

if play == "Y":  
    game_on = True
    
    # Declare variables & draw first card for each player
    player_1 = random.choice(cards)
    comp = random.choice(cards)

    player_1 += random.choice(cards)
    comp += random.choice(cards)

    while game_on:
        ## FOR TESTING 
        # print(f"player 1 score: {player_1}")
        # print(f"comp score: {comp}")

        # Draw another card for comp if hand is below 17
        if comp < 17:
            comp = draw_card(comp)

        if player_1 < 21:
            # Ask user if they would like to draw another card
            deal = input(f"Your hand is {player_1}. Would you like to draw another card? Y/N : ").upper()

            if deal == "Y":
                player_1 = draw_card(player_1)

        # Check card of players 
        game_on = check_cards(player_1, comp)
            
print("Game has ended.")



