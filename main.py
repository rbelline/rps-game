from enum import Enum
import random

class Shapes(Enum):
    ROCK = "rock"
    SCISSOR = "scissor"
    PAPER = "paper"

class Player:
    def __init__(self):
        self.score = 0
        self.shapes = [Shapes.ROCK.name, Shapes.SCISSOR.name, Shapes.PAPER.name]
        self.name = "player"

    def choose(self):
        while True: 
            user_input = input("Please enter your choice (rock, scissor, paper): ").upper()
            if user_input in self.shapes:
                print(f"player chose: {user_input}")
                return user_input
            print("Invalid option. Please try again (rock, scissor, paper): ")

class Computer:
    def __init__(self):
        self.score = 0
        self.shapes = [Shapes.ROCK.name, Shapes.SCISSOR.name, Shapes.PAPER.name]
        self.name = "computer"

    def choose(self):
        choice = random.choice(self.shapes)
        print(f"computer chose: {choice}")
        return choice
    
class Game:
    def __init__(self):
        self.title = "Rock Paper Scissor Game"
        self.max_rounds = 3
        self.round = 0
        self.computer = Computer()
        self.player = Player()
        print(f"welcome to {self.title}")

    def play(self):
        while (self.round < self.max_rounds):
            player_choice = self.player.choose()
            computer_choice = self.computer.choose()
            self.adjust_score(computer_choice, player_choice)
            # self.define_round()
            self.display_scores()
        winner = self.determine_winner()
        print(f"{winner} WON!")
            # print(f"this is the round: {self.round}")
            # print(f"this is the max number of round: {self.max_rounds}")
            # print(f"this is the player score: {self.player.score}")
            # print(f"this is the computer score: {self.computer.score}")

    def adjust_score(self, computer_choice, player_choice):
        #rock > scissor
        #scissor > paper
        #paper > rock
        if computer_choice == player_choice:
            print("it's even")
            return
        if (
            computer_choice == Shapes.ROCK.name and player_choice == Shapes.SCISSOR.name or \
            computer_choice == Shapes.SCISSOR.name and player_choice == Shapes.PAPER.name or \
            computer_choice == Shapes.PAPER.name and player_choice == Shapes.ROCK.name
            ):
            self.computer.score += 1
        else:
            self.player.score += 1
        self.round += 1
    
    def determine_winner(self):
        return self.computer.name if self.computer.score > self.player.score else self.player.name

    def define_round(self):
        print(f"round number {self.round}")
    
    def display_scores(self):
        print(f"{self.player.name} score: {self.player.score}")
        print(f"{self.computer.name} score: {self.computer.score}")
    
if __name__ == "__main__":
    print("This is the main file")
    game = Game()
    game.play()