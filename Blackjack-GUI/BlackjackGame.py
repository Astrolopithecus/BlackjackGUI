# Miles Philips
# Prog 120
# Final ProjectProject Phase 3
# Blackjack program
# 5-31-19 

#!/usr/bin/env python3

from objects import Card, Deck, Hand

class Blackjack:
    def __init__(self, startingBalance):
        self.money = startingBalance
        self.deck = Deck()
        self.playerHand = Hand()
        self.dealerHand = Hand()
        self.bet = 0

    def displayCards(self,hand, title):
        ''' Print the title and display the cards in the given hand in a sorted order'''
        print(title.upper())        
        for c in sorted(hand):
            print(c)
        print()

    def handle_winner(self, winner, message):
        ''' print the player's hand's points
        print the message
        Update self.money according to the winner
        '''
        print("Your Points: ", self.playerHand.points)
        print("Dealer Points: ", self.dealerHand.points)
        print(message)
        if winner == "player":
            print("foo", self.money, self.bet)
            self.money += self.bet
        elif winner == "dealer":
            self.money -= self.bet
        elif winner == "tie":
            pass
        elif winner == "blackjack":
            self.money += (1.5*self.bet)
        
    def getBet(self):
        ''' Method to update self.bet by prompting the user for the bet amount,
        making sure bet is less than self.money.
        '''
        while True:
            try:
                bet = int(input("What is your bet:  "))
                if bet <= self.money and bet > 0:
                    self.bet = bet
                    return False
                elif bet > self.money:
                    print("You don't have that much money")
            except ValueError:
                print("You must enter a positive number!")
                
    def setupRound(self):
        ''' Setup the round by doing these steps:
        Call getBet to initialize self.bet,
        initialize self.deck to a new Deck object and shuffle it
        initialize self.dealerHand and self.playerHand to new Hand objects
        deal two cards to the playerHand, and one card to the dealerHand
        finally, print dealerHand and playerHand using displayCards method
        '''
        self.getBet()
        self.deck = Deck()
        self.deck.shuffle()
        self.dealerHand = Hand()
        self.playerHand = Hand()
        self.dealerHand.addCard(self.deck.dealCard())
        self.playerHand.addCard(self.deck.dealCard())
        self.playerHand.addCard(self.deck.dealCard())
        Blackjack.displayCards(self,self.dealerHand,"Dealer")
        Blackjack.displayCards(self,self.playerHand,"Player")
        
    def play_playerHand(self):
        ''' Method to implement player playing his hand by
        1. Prompting the user to indicate Hit (h) or Stand (s)
        2. If user picks stand, end the player play by returning
        3. If user picks hit,
            deal a card to the playerHand.
            check if with the latest addition, the hand busts (has > 21 points), if so return
            otherwise, prompt the player again whether to hit or stand.
        4. Print playerHand points
        '''
        while True:
            pick = input('\nPress "h" to hit or "s" to stand:  ')
            if pick.lower() == "h":
                self.playerHand.addCard(self.deck.dealCard())
                Blackjack.displayCards(self,self.playerHand,"Player Hand")
                
                if self.playerHand.points > 21:
                    return False
                else:
                    continue
            elif pick.lower() == "s":
                return False
            else:   
                print("Not a valid command! Please try again.")
            
    def play_dealerHand(self):
        ''' Method to play the dealer's hand.
        Continue to deal cards till the points of the dealerHand are
        less than 17. Print the dealer's hand before returning'''
        dealerHandValue = self.dealerHand.points
        while dealerHandValue < 17:
            self.dealerHand.addCard(self.deck.dealCard())
            dealerHandValue = self.dealerHand.points
        Blackjack.displayCards(self,self.dealerHand,"Dealer")
            
    def playOneRound(self):
        ''' Method implements playing one round of the game
        1. Checks if playerHand is a Blackjack, if so handles that case
        2. Lets player play his hand if it busts, declares player loser
        3. Else lets dealer play his hand.
        4. If dealer busts, declares the player to be the winner
        5. Otherwise declares the winner based on who has higher points:
            if Player > dealer, player is the winner
            else if player < dealer, dealer is the winner
            else it is a tie        
        '''
        playerHandValue = self.playerHand.points
        if playerHandValue == 21:
            Blackjack.handle_winner(self,"blackjack","You got Blackjack!")

        else:
            Blackjack.play_playerHand(self)
            playerHandValue = self.playerHand.points
            if playerHandValue > 21:
                Blackjack.handle_winner(self,"dealer","You went bust!")
                    
            else:
                Blackjack.play_dealerHand(self)
                dealerHandValue = self.dealerHand.points
                if dealerHandValue > 21:
                    Blackjack.handle_winner(self,"player","Dealer went bust, you win!")
                        
                elif playerHandValue > dealerHandValue:
                    Blackjack.handle_winner(self,"player","You win!")
                        
                elif playerHandValue < dealerHandValue:
                    Blackjack.handle_winner(self,"dealer","You lose!")
                        
                elif playerHandValue == dealerHandValue:
                    Blackjack.handle_winner(self,"tie","It's a tie!")
                        
                            
def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    # initialize starting money
    startbal = 100
    print("Starting Balance:", startbal)

    blackjack = Blackjack(startbal)
    # start loop
    again = 'y'
    while again.lower() == 'y':

        print("Setting up a round...")
        blackjack.setupRound()

        print("Playing Player Hand...")
        blackjack.playOneRound()
        print("You have " , blackjack.money , " dollars.")

        print()
        again = input("Play again? (y/n): ").lower()
        print()
        if again != "y":
            break

    print("Bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
