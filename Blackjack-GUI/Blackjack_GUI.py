##Miles Philips
##GUI version of the Blackjack game.
##10-1-19

from BlackjackGame import Blackjack
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# define GameFrame class that is derived from Frame class
class GameFrame(tk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.blackjack = Blackjack(100)

        # Define string variables for text entry fields
        self.playerHand = tk.StringVar()
        self.dealerHand = tk.StringVar()
        self.money = tk.StringVar()
        self.bet = tk.StringVar()

        # calls initComponents
        self.initComponents()

    # define initComponents module
    def initComponents(self):
        self.pack()

        # Display grid of labels and text entry fields
        self.LabelA= ttk.Label(self, text="Player Hand").grid(column=0, row=0, sticky=tk.E)
        self.EntryA = ttk.Entry(self, width=15, textvariable=self.playerHand, state ="readonly").grid(column=1, row=0)

        self.LabelB= ttk.Label(self, text="Dealer Hand").grid(column=0, row=1, sticky=tk.E)
        self.EntryB = ttk.Entry(self, width=15, textvariable=self.dealerHand, state ="readonly").grid(column=1, row=1)

        self.LabelC = ttk.Label(self, text="Wallet").grid(column=0, row=2, sticky=tk.E)
        self.EntryC = ttk.Entry(self, width=15, textvariable=self.money, state ="readonly").grid(column=1, row=2)

        self.LabelD = ttk.Label(self, text="Bet").grid(column=0, row=3, sticky=tk.E)
        self.EntryD = ttk.Entry(self, width=15, textvariable=self.bet, state ="readonly").grid(column=1, row=3)

        self.makeButtons()

               
    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=0, row=4, columnspan=2, sticky=tk.E)

        # Add three buttons to the button frame
        ttk.Button(buttonFrame, text="Hit", command=self.calculateMPG) \
            .grid(column=0, row=0, padx=5)
        ttk.Button(buttonFrame, text="Stand", command=self.parent.destroy) \
            .grid(column=1, row=0)
        ttk.Button(buttonFrame, text="New Game", command=self.newgame) \
            .grid(column=2, row=0)
        ttk.Button(buttonFrame, text="Quit", command=self.parent.destroy) \
            .grid(column=3, row=0, padx=5)
        
    # defines a method for setting up game
    def newgame(self):
        self.money.set(100)
        self.blackjack.dealerHand.addCard(self.blackjack.deck.dealCard())
        self.blackjack.playerHand.addCard(self.blackjack.deck.dealCard())
        self.playerHand.set(self.blackjack.playerHand)
        self.dealerHand.set(self.blackjack.dealerHand)
        

    # defines a method for calculating MPG
    def calculateMPG(self):

        mil = self.dvA.get()
        gal = self.dvB.get()

        # verify entered values are positive number or displays error message 
        if (mil >= 0) and (gal > 0):
            MPG = self.mpg.calculate(mil,gal)
            MPG = round(MPG, 2)
            self.dvC.set(MPG) 
        else:
            messagebox.showerror("Error", "Please enter positive numbers!")

    # define a method for clearing entry fields
    def clear(self):    
        self.dvA.set("")
        self.dvB.set("")
        self.dvC.set("")

# define main function
def main():
    root = tk.Tk()
    root.geometry("440x220")
    root.title("MPG Calculator")
    GameFrame(root)

    root.mainloop()
    

if __name__ == "__main__":
    main()
