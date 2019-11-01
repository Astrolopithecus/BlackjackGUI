# Miles Philips
# Prog 120
# Final ProjectProject Phase 2
# objects
# 5-31-19 

#!/usr/bin/env python3
import random
CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}
RANKORDER = { "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10": 10, "Jack":11, "Queen":12, "King": 13, "Ace": 14}

##########################################################################
## Definitions for the classes: Card, Deck and Hand
##########################################################################

#create Card class
class Card:

    # initialize
    def __init__(self, suit, rank):
        self.__rank = rank
        self.__suit =suit

    # define value property
    @property
    def value(self):
        if self.__rank == "Ace":
            v = 11
        elif self.__rank in ("Jack", "Queen", "King"):
            v = 10
        else:
            v = int(self.__rank)
        return v

    # define string module 
    def __str__(self):
        return str(self.__rank) + " of " + str(self.__suit) + CARDS_CHARACTERS[self.__suit]
##
##    # define less than function
##    def __le__(self, other):
##        return (self.__suit,RANKORDER[self.__rank]) <= (other.__suit,RANKORDER[other.__rank]) 

# define greater than function
    def __gt__(self, other):
        return (self.__suit,RANKORDER[self.__rank]) > (other.__suit,RANKORDER[other.__rank]) 
    
##    # define displayCard module 
##    def displayCard(self):
##        card = str(self.__rank) + " of " + str(self.__suit) + CARDS_CHARACTERS[self.__suit]
##        return card
##    
        
#create Deck class
class Deck:
    
    # initialize a deck of 52 cards
    def __init__(self):
        self.__deck = []
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for r in suits:
            for s in ranks:
                c = Card(r,s)
                self.__deck.append(c) 

    # define iter function     
    def __iter__(self):
        for card in self.__deck:
            yield card

##    # define count property   
##    @property
##    def count(self):    
##        self.__count = len(self.__deck)
##        return self.__count

    # define len function
    def __len__(self):
        return len(self.__deck)

    # define shuffle property
    def shuffle(self):
        random.shuffle(self.__deck)

    # define dealCard property
    def dealCard(self):
        return self.__deck.pop()
    
# create Hand class
class Hand:
    
    # initialize 
    def __init__(self):
        self.__cards = []

    # define iter function
    def __iter__(self):
        for card in self.__cards:
            yield card

# define greater than function
    def __gt__(self, other):
        return (self.points) > (other.points) 
    

##    # define count property
##    @property
##    def count(self):    
##        count = len(self.__cards)
##        return count

    # define len function
    def __len__(self):
        return len(self.__cards)

    # define points property
    @property
    def points(self):
        points = 0
        for c in self.__cards:
            points += c.value
        return points
    
    # define addCard method
    def addCard(self,card):
        self.__cards.append(card)
        return self.__cards
        
    # define displayHand method
    def displayHand(self):
        for h in self.__cards:
            print(h)
            #h.displayCard()

# define main function        
def main():
    print("Cards - Tester")
    print()

    #test sorting of the cards
    testcardsList = [Card("Spades","Ace"), Card("Hearts","Queen"), Card("Clubs","10"),
             Card("Diamonds", "3"), Card("Hearts","Jack"), Card("Spades","7")]
    testcardsList.sort()
    print("TEST CARDS LIST AFTER SORTING.")
    for c in testcardsList:
        print(c)
    print()

    # test deck
    print("DECK")
    deck = Deck()
    print("Deck created.")
    deck.shuffle()    
    print("Deck shuffled.")
    print("Deck count:", len(deck))
    print()

    # test hand
    hand = Hand()
    for i in range(10):
        hand.addCard(deck.dealCard())

    print("SORTED HAND")
    for c in sorted(hand):
        print(c)

    print()
    print("Hand points:", hand.points)
    print("Hand count:", len(hand))
    print("Deck count:", len(deck))

if __name__ == "__main__":
    main()
