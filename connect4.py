class Board:
    #function1
    def __init__(self,height,width):
        """constructs a new board object by initializing the three attributes."""

        self.height=height
        self.width=width
        self.slots = [[' '] * self.width for row in range(self.height)]
    #function2
    def __str__(self):
        """returns a string representing a Board object."""
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        s+= ('-'*(2*col+3))
        s+='\n'
        for row in range(self.width):
            if row>9:
                s+= ' ' + str(row-10)
            else:
                s+= ' ' + str(row)
        return s
    #function3
    def __repr__(self):
        """ retruns a string representing the called Board object. """

        return str(self)
    #function4
    def add_checker(self,checker,col):
        """ adds either a x or o in the appropriate column. """

        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row=0
        while self.slots[row][col]==' ' and row<self.height:
            row+=1
            if row>=self.height-1:
                break
        if self.slots[row][col] != ' ':
            self.slots[row-1][col]=checker
        else:
            self.slots[row][col]=checker
    #function5
    def clear(self):
        """ clears the Board object on which it is called by setting
        all slots to contain a space character."""

        for i in range(self.height):
            for j in range(self.width):
                self.slots[i][j]= ' '
    #function6
    def add_checkers(self, colnums):
        """takes in a string of column number and places alternating
           checkers in those columns of the called Board object,
           starting with 'X'.
        """
        checker = 'X' # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    #function7
    def can_add_to(self, col):
        """ retrun True if it is valid to place a checker in the
            column col on the calling Board object.
        """

        if col < 0 or col >= self.width:
            return False
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False
    #function8
    def is_full(self):
        """ return True if the called Board object is completely full.
        """
        for i in range(self.width):
            empty=self.can_add_to(i)
            if empty == True:
                return False
        return True
    #function9
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board
            object.
        """
        row=0
        while row < self.height:
            if self.slots[row][col]!= ' ':
                self.slots[row][col]=' '
                break
            else:
                row+=1
    #function10.a
    def is_horizontal_win(self, checker):
        """ Checkes for a horizontal win for the specified checker.
        """

        for row in range(self.height):
            for col in range(self.width - 3):
                # check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col+1] == checker and \
                   self.slots[row][col+2] == checker and \
                   self.slots[row][col+3] == checker:
                    return True
        return False
    #function10.b
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """

        for row in range(self.height-3):
            for col in range(self.width ):
                # check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False
    #function10.c
    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonals that go down from left to right
            win for the specified checker.
        """

        for row in range(self.height-3):
            for col in range(self.width-3):
                # check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False
    #function10.d
    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonals that go up from left to right
            win for the specified checker.
        """

        for row in range(self.height):
            for col in range(self.width-3):
                # check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
                
        return False
    #function10
    def is_win_for(self, checker):
        """ accpets a parameter checker that is either 'X' or 'O', and
            returns True if there are four consecutive slots containing
            checker on the board.
        """
        assert(checker == 'X' or checker == 'O')

        horz=self.is_horizontal_win(checker)
        vert=self.is_vertical_win(checker)
        updiag=self.is_up_diagonal_win(checker)
        downdiag=self.is_down_diagonal_win(checker)

        if horz==True or vert==True or\
           updiag==True or downdiag==True:
            return True
        else:
            return False
        
#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#
# name: Priyank Shroff
# email: shroffp@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from ps10pr1 import Board

# Write your Player class below.
class Player:
    #function1
    def __init__(self, checker):
        """ Constructs a new PLayer object.
        """
        assert(checker == 'X' or checker == 'O')
        self.checker=checker
        self.num_moves= 0

    #function2
    def __str__(self):
        """ returns a string representing a Player object.
        """
        x= 'Player'
        return x + ' ' + self.checker

    #function3
    def __repr__(self):
        """ returns a string representing a Player object.
        """
        return str(self)
    #function4
    def opponent_checker(self):
        """ returns a one-character string representing the
            checker of the Player objects opponent.
        """
        if self.checker == 'X' :
            return 'O'
        else:
            return 'X'
    #function5
    def next_move(self, board):
        """ accepts a Board object as a parameter and returns
            the column where the player wants to make the next
            move.
        """

        colno=int(input('Enter a column:'))
        while board.can_add_to(colno)==False:
            print('Try again!')
            colno=int(input('Enter a column:'))
        self.num_moves+=1
        return colno
#
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Playing the game!
#
# name: Priyank Shroff
# email: shroffp@bu.edu
#
# This is an individual-only problem that you must complete on your own,
# without a partner.
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One of them should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure that one is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board
def process_move(player, board):
    """ perfroms all the steps involved in processing a single move by the
              specified player on the specified board.
    """
    print(str(player)+"'s"+ ' '+ 'turn')
    
    nextmove=player.next_move(board)
    
    if board.can_add_to(nextmove)==True:
        addcheck=board.add_checker(player.checker,nextmove)

    print()    
    print(board)
    
    wol=board.is_win_for(player.checker)
    
    if wol==True:
        print(player, 'wins in', player.num_moves,'moves')
        print('Congratualations!')
        return True
    elif wol==False:
        full=board.is_full()
        if full==True:
            print('Its a tie!')
            return True
        else:
            return False
class RandomPlayer(Player):
    def next_move(self, board):
        """ chooses at random from the columns in the specified
                            board.
        """
        collst=[]
        for col in range(board.width):
            if board.can_add_to(col)==True:
                collst+=[col]
        self.num_moves+=1
        colno=random.choice(collst)
        return colno

#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# An AI Player for Connect Four
#
# name: Priyank Shroff
# email: shroffp@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from ps10pr3 import *
import random

class AIPlayer(Player):

    #function1
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AI Object.
        """

        assert(checker == 'X' or checker == 'O')
        assert(tiebreak=='LEFT' or tiebreak=='RIGHT' or tiebreak=='RANDOM')
        assert(lookahead >= 0)

        Player.__init__(self, checker)
        self.tiebreak=tiebreak
        self.lookahead=lookahead

    #function2
    def __str__(self):
        """ returns the string representing an AIPlayer object.
        """

        x='Player'+' '+self.checker + ' ' +'('+ str(self.tiebreak) + ',' + ' ' +str(self.lookahead)+ ')'
        return x
    
    #function3
    def max_score_column(self, scores):
        """ takes a list scores containing a score for
            each column of the board, and returns the
            index of the column with the maximum score.
        """

        max_score=max(scores)
        lst=[]
        for i in range(len(scores)):
            if max_score==scores[i]:
                lst+=[i]
        if self.tiebreak=='LEFT':
            return lst[0]
        elif self.tiebreak=='RIGHT':
            return lst[-1]
        else:
            return random.choice(lst)

    #function4
    def scores_for(self, board):
        """ takes a Board object board and determines
              the called AIPlayer's score for the
                   columns in board.
        """
        scores=[' ']*board.width
        for i in range(board.width):
            if board.can_add_to(i)==False:
                scores[i]=-1
            elif board.is_win_for(self.checker)==True:
                scores[i]=100
                print(b)
            elif board.is_win_for(self.opponent_checker())==True:
                scores[i]=0
            elif self.lookahead==0:
                scores[i]=50
            else:
                board.add_checker(self.checker,i)
                if self.checker=='X':
                    opp=AIPlayer('O',self.tiebreak, (self.lookahead)-1)
                else:
                    opp=AIPlayer('X',self.tiebreak, (self.lookahead)-1)
                rest=opp.scores_for(board)
                max_score=max(rest)
                scores[i]=100-max_score
                board.remove_checker(i)
        return scores

    #function5
    def next_move(self, board):
        """ chooses the best column in the specified
                            board.
        """
        score_b=self.scores_for(board)
        max_col=self.max_score_column(score_b)
        self.num_moves+=1

        return max_col






