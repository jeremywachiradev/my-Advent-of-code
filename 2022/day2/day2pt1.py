import enum
"""
I MESSED SOMETHING UP IN THIS FILE ... ILL CHECK LATER, MAYBE NOT TOO 
"""
input="""
A Y
B X
C Z
"""

class Player:
    def __init__(self):
        self.score=0
        self.move=None
        self.is_winner=False
        self.symbol=None
    def update_winner(self):
        self.is_winner=True

class Move(enum.Enum):
    ROCK ="Rock"
    PAPER="Paper"
    SCISSORS="Scissors"

class Game:
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
    

    def play(self,input):
        
        input=input.strip().split("\n")
        
        for game in input:
            self.player1.symbol,self.player2.symbol=game.split()
            if self.player1.symbol=="A":
                self.player1.move=Move.ROCK
            elif self.player1.symbol=="B":
                self.player1.move=Move.PAPER
            elif self.player1.symbol=="C":
                self.player1.move=Move.SCISSORS

            if self.player2.symbol=="X":
                self.player2.move=Move.ROCK
            elif self.player2.symbol=="Y":
                self.player2.move=Move.PAPER
            elif self.player2.symbol=="Z":
                self.player2.move=Move.SCISSORS
            self.score_calculator(self.player1,self.player2)
            
            # print(f"The score for player1: {self.player1.score} and that of player2 is : {self.player2.score}")
        return self.player2.score
        
    def score_calculator(self,player1,player2):
        if player1.move==Move.ROCK:
            match player2.move:
                case Move.ROCK:
                    player1.score+=4
                    player2.score+=4
                case Move.PAPER:
                    player1.score+=1
                    player2.score+=8

                case Move.SCISSORS:
                    player1.score+=7
                    player2.score+=3


        elif player1.move==Move.PAPER:
            match player2.move:
                case Move.ROCK:
                    player1.score+=8
                    player2.score+=1
                case Move.PAPER:
                    player1.score+=5
                    player2.score+=5

                case Move.SCISSORS:
                    player1.score+=2
                    player2.score+=9

        elif player1.move==Move.SCISSORS:
            match player2.move:
                case Move.ROCK:
                    player1.score+=3
                    player2.score+=7
                case Move.PAPER:
                    player1.score+=9
                    player2.score+=2

                case Move.SCISSORS:
                    player1.score+=6
                    player2.score+=6

        
player1=Player()
player2=Player()
my_game=Game(player1,player2)
print(my_game.play(input))