import random

class Stack:
    """Stack class implementation"""
    def __init__(self):
        """initialises a stack class with an empty python list"""
        self.stack_list = []

    def __str__(self):
        """
        returns a string representation of the stack
        """
        values = []
        for x in self.cards:
            rank = x[0][0] if x[0][0] else x[0][1]
            values.append(str(rank)+' '+'of'+' '+str(x[1]))
        return '\n'.join(values)

    def size(self):
        """
        returns the size of the stack
        """
        return len(self.stack_list)

    def push(self, e):
        """adds an element to the stack"""
        if self.size <= 5:
            self.stack_list.append(e)
            return e
        return None

    def pop(self):
        """
        removes an item from the stack and return it
        """
        if self.empty():
            return "Empty Stack, nothing to pop."
        return self.stack_list.pop()

    def top(self):
        """
        returns the top element
        """
        if self.empty():
            return
        return self.stack_list[-1]

    def empty(self):
        """checks if the stack is empty"""
        if self.stack_list == []:
            return True
        return False

class Deck:
    def __init__(self):
        """
        initialise the 'Deck' class
        """
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = [('Ace',1),(None,2), (None,3), (None,4), (None,5), (None,6), (None,7), (None,8), (None,9), (None,10), ('Jack', 11), ('Queen', 12), ('King', 13)]
        self.cards = []
        for s in self.suits:
            for r in self.ranks:
                self.cards.append((r,s))

    def __str__(self):
        """
        string respresentation of the 'Deck' class
        """
        values = []
        for x in self.cards:
            rank = x[0][0] if x[0][0] else x[0][1]
            values.append(str(rank)+' '+'of'+' '+str(x[1]))
        return '\n'.join(values)

    def shuffle(self):
        """
        method that shuffles the cards list
        """
        random.shuffle(self.cards)

class Card:
    def __init__(self):
        """
        initialise the 'Card' class
        """
        self.deck = Deck()

    def print_cards(self, cards_list):
        """
        method that prints the cards in the expected format
        """
        values = []
        count = 1
        for x in cards_list:
            rank = x[0][0] if x[0][0] else x[0][1]
            values.append(str(count)+'. '+str(rank)+' '+'of'+' '+str(x[1]))
            count += 1
        return '\n'.join(values)

    def play(self, user):
        """
        method to create game play instance
        """
        self.deck.shuffle()
        print('\t\n====={} is playing====\n'.format(user))
        player = Stack()
        count = 0
        my_cards = []
        for card in self.deck.cards:
            count += 1
            rank = card[0][0] if card[0][0] else card[0][1]
            print(str(rank)+' '+'of'+' '+str(card[1]))
            card_choice = str(input())
            nos_count = 0
            if card_choice == 'no':
                nos_count += 1
                if count <= 5:
                    pass
                else:
                    my_cards.append(card)
            elif card_choice == 'yes':
                my_cards.append(card)

            if count >= 10:
                break

        for i in range(len(my_cards)):
            print("\t\n****select card****\n")
            print(self.print_cards(my_cards))
            card_no = int(input())
            player.push(my_cards.pop(card_no-1))

        return player

    def points(self):
        """
        - method to calculate ponts for the two players
        - calls the 'play' method
        """
        p1 = 'Player-1'
        p2 = 'Player-2'
        play_1 = self.play(p1)
        play_2 = self.play(p2)
        total_score_1 = 0
        total_score_2 = 0
        
        for i in range(play_1.size()):
            score_1 = play_1.pop()
            score_2 = play_2.pop()
            if int(score_1[0][1]) > int(score_2[0][1]):
                msg = p1
            elif int(score_1[0][1]) == int(score_2[0][1]):
                if score_1[1] > score_2[1]:
                    msg = p1
                else:
                    msg = p2
            else:
                msg = p2
            total_score_1 += int(score_1[0][1])
            total_score_2 += int(score_2[0][1])
            print("{} won turn {}\nThe score of Player-1 {}\nThe score of Player-2 {}\n".format(msg, i+1, score_1[0][1], score_2[0][1]))
        if total_score_1 > total_score_2:
            response = [p1, total_score_1]
        else:
            response = [p2, total_score_2]

        print("Congratulations {}! You have earned {} points and won the game.".format(response[0],response[1]))



if __name__ == '__main__':
    c = Card()
    c.points()