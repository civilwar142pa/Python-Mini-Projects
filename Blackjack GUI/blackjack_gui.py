import customtkinter as ctk
import art
import random

#CLASSES

class myTitleFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        mono_font = ctk.CTkFont(family="Courier", size=12, weight="normal")
        
        self.label = ctk.CTkLabel (
            self,
            text=art.logo,
            font=mono_font,
            justify="center"
        )
        self.label.grid(row=0, column=0, padx=20, pady=0, sticky="ew", columnspan=3)

class myPlayerFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # main player frame
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #card subframe
        self.card_container = ctk.CTkFrame(self, fg_color="transparent")
        self.card_container.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        #score subframe
        self.score_container = ctk.CTkFrame(self, fg_color="transparent")
        self.score_container.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        #labels
        self.score_label = ctk.CTkLabel(self.score_container, text="Player Score: 0")
        self.score_label.pack(expand=True)
        
class myDealerFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #card subframe
        self.card_container = ctk.CTkFrame(self, fg_color="transparent")
        self.card_container.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        #score subframe
        self.score_container = ctk.CTkFrame(self, fg_color="transparent")
        self.score_container.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        #labels
        self.score_label = ctk.CTkLabel(self.score_container, text="Dealer Score: 0")
        self.score_label.pack(expand=True)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#MAIN PROGRAM
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("BlackJack w/ GUI")
        self.geometry("600x500")
        ctk.set_appearance_mode("system")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.myTitleFrame = myTitleFrame(self)
        self.myTitleFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=2)

        self.myPlayerFrame = myPlayerFrame(self)
        self.myPlayerFrame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        
        self.myDealerFrame = myDealerFrame(self)
        self.myDealerFrame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        
        self.start_game_button = ctk.CTkButton(self, text="New Game", command=self.start_game, fg_color="green")
        self.start_game_button.grid(row=2, column=0, padx=20, pady=15, sticky="ew", columnspan=1)
        
        self.end_game_button = ctk.CTkButton(self, text="End Game", command=self.button_callback, fg_color="red")
        self.end_game_button.grid(row=2, column=1, padx=20, pady=15, sticky="ew", columnspan=1)
        
        #initialize game state
        self.pcards = []
        self.dcards = []
        self.pscore = 0
        self.dscore = 0
        
    
    #FUNCTION
    
    def start_game(self):
        self.initial_cards()
        self.scores()
        self.main_display()
        self.compare()
        self.myPlayerFrame.score_label.configure(text=f"Player Score: {self.pscore}")
        self.myDealerFrame.score_label.configure(text=f"Dealer Score: {self.dscore}")
        self.myPlayerFrame.card_container.configure(text=f"Player Cards: {self.pcards}")
        self.myDealerFrame.card_container.configure(text=f"Dealer Cards: {self.dcards[0]} and ?")

    def initial_cards(self):
        """randomizes two cards from the deck for player and dealer"""
        self.pcards = [random.choice(cards), random.choice(cards)]
        self.dcards = [random.choice(cards), random.choice(cards)]
        return self.pcards, self.dcards


    def new_card(self):
        """randomizes a new card"""
        return random.choice(cards)


    def scores(self):
        """Calculates player and dealer scores"""
        self.pscore = sum(self.pcards)
        self.dscore = sum(self.dcards)

        # Check the card lists for the Ace (11), not the pscore integer
        while self.pscore > 21 and 11 in self.pcards:
            self.pscore -= 10
            self.pcards.remove(11)
            self.pcards.append(1)

        while self.dscore > 21 and 11 in self.dcards:
            self.dscore -= 10
            self.dcards.remove(11)
            self.dcards.append(1)

        return self.pscore, self.dscore


    def main_display(self):
        self.myPlayerFrame.label.configure(text=f"Your cards: {self.pcards} | Current score: {self.pscore}")
        self.myDealerFrame.label.configure(text=f"Dealer's first card: {self.dcards[0]}")


    def compare(self):
        if self.pscore > 21:
            self.myPlayerFrame.label.configure(text="You went Bust! Better luck next time!")
            self.myDealerFrame.label.configure(text="Dealer wins!")
            self.is_game_over = True
            return self.is_game_over

        if self.dscore == 21:
            self.myPlayerFrame.label.configure(text="Dealer has Blackjack! Better luck next time!")
            self.myDealerFrame.label.configure(text="Dealer has 21! Blackjack! Dealer wins!")
            self.is_game_over = True
            return self.is_game_over

        if self.pscore == 21 and self.dscore != 21:
            self.myPlayerFrame.label.configure(text="Blackjack! You win!")
            self.myDealerFrame.label.configure(text="Dealer loses!")
            self.is_game_over = True
            return self.is_game_over

        else:
            self.is_game_over = False
            return self.is_game_over


    def end_score(self):
        if self.dscore > 21:
            self.myPlayerFrame.label.configure(text="You win!")
            self.myDealerFrame.label.configure(text="Dealer went Bust!")

        elif self.pscore > self.dscore:
            self.myPlayerFrame.label.configure(text="You win!")
            self.myDealerFrame.label.configure(text="Dealer loses!")

        elif self.dscore > self.pscore:
            self.myPlayerFrame.label.configure(text="You lose. Better luck next time!")
            self.myDealerFrame.label.configure(text="Dealer wins!")

        elif self.dscore == self.pscore:
            self.myPlayerFrame.label.configure(text="It's a draw!")
            self.myDealerFrame.label.configure(text="Dealer also draws!")


    def end_display(self):
        self.myPlayerFrame.label.configure(text=f"Your cards: {self.pcards} | Final score: {self.pscore}")
        self.myDealerFrame.label.configure(text=f"Dealer's cards: {self.dcards} | Final score: {self.dscore}")


    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()