import art
import random

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# FUNCTIONS
def initial_cards():
    """randomizes two cards from the deck for player and dealer"""
    pcards = [random.choice(cards), random.choice(cards)]
    dcards = [random.choice(cards), random.choice(cards)]
    return pcards, dcards
    #FINISHED


def new_card():
    """randomizes a new card"""
    return random.choice(cards)


def scores(pcards, dcards):
    """Calculates player and dealer scores"""
    pscore = sum(pcards)
    dscore = sum(dcards)

    # Check the card lists for the Ace (11), not the pscore integer
    while pscore > 21 and 11 in pcards:
        pscore -= 10
        pcards.remove(11)
        pcards.append(1)

    while dscore > 21 and 11 in dcards:
        dscore -= 10
        dcards.remove(11)
        dcards.append(1)

    return pscore, dscore
    #FINISHED


def main_display(pcards, dcards, pscore):
    print(f"Your cards: {pcards} | Current score: {pscore}\n")
    print(f"Dealer's first card: {dcards[0]}")


def compare(pscore, dscore, pcards, dcards):
    if pscore > 21:
        print(f"\n{art.loser}")
        print("\n--- You went bust! Better luck next time! ---")
        is_game_over = True
        return is_game_over

    if dscore == 21:
        print(f"\n{art.loser}")
        print("\n--- Dealer has 21! You lose. Better luck next time! ---")
        is_game_over = True
        return is_game_over

    if pscore == 21 and dscore != 21:
        print(f"\n{art.winner}")
        print("\n--- Blackjack! You win! ---")
        is_game_over = True
        return is_game_over

    else:
        is_game_over = False
        return is_game_over


def end_score(pscore, dscore,pcards, dcards):
    if dscore > 21:
        print(f"\n{art.winner}")
        print("--- Dealer busts! You win! ---")

    elif pscore > dscore:
        print(f"\n{art.winner}")
        print("--- You win! ---")

    elif dscore > pscore:
        print(f"\n{art.loser}")
        print("--- You lose. Better luck next time! ---")

    elif dscore == pscore:
        print(f"\n{art.draw}")
        print("--- It's a draw! ---")


def end_display(pcards, dcards, pscore, dscore):
    print(f"Your cards: {pcards} | Final score: {pscore}\n")
    print(f"Dealer's cards: {dcards} | Dealer score: {dscore}")


# MAIN PROGRAM
another_game = input("Do you want to play a game of blackjack(y/n): ")
while another_game == "y":
    print("\n" + "="*30)
    #initial deal, scores and display
    pcards, dcards = initial_cards()
    pscore, dscore = scores(pcards, dcards)
    main_display(pcards, dcards, pscore)

    #compare scores and check for blackjack
    is_game_over = compare(pscore, dscore, pcards, dcards)


    while not is_game_over:
        #get new scores
        pscore, dscore = scores(pcards, dcards)
        is_game_over = compare(pscore, dscore, pcards, dcards)

        if not is_game_over:
            print("-"*20)
            another_card = input("\nType 'y' to draw another card, 'n' to pass: ")
            if another_card == "y":
                # draw card
                pcards.append(new_card())
                pscore,dscore = scores(pcards, dcards)
                #display
                main_display(pcards, dcards, pscore)

            elif another_card == "n":
                while dscore < 17:
                    # draw card
                    dcards.append(new_card())
                    # get new scores
                    pscore, dscore = scores(pcards, dcards)
                    print("Dealer has drawn a card.")
                if dscore >= 17:
                    is_game_over = True

    if is_game_over:
        print("GAME OVER")
        end_score(pscore,dscore,pcards,dcards)
        end_display(pcards, dcards, pscore, dscore)

    another_game = input("Do you want to play again? (y/n): ").lower()

print("\nSee you next time!")