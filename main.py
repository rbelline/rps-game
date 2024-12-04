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

    def choose(self):
        print(self.shapes)
        while True:
            user_input = input("Please enter your choice (rock, scissor, paper): ").upper()
            print(user_input)
            if user_input in self.shapes:
                return user_input
            print("Invalid option. Please try again (rock, scissor, paper): ")

class Computer:
    def __init__(self):
        self.score = 0
        self.shapes = [Shapes.ROCK.name, Shapes.SCISSOR.name, Shapes.PAPER.name]

    def choose(self):
        shape_of_choice = random.choice(self.shapes)
        print(shape_of_choice)
        return shape_of_choice
    
class Game:
    def __init__(self):
        self.title = "Rock Paper Scissor Game"
        self.max_rounds = 3
        self.round = 0
        self.computer = Computer()
        self.palyer = Player()
        print(f"welcome to {self.title}")

    def play(self):
        self.computer.choose()
        self.palyer.choose()


if __name__ == "__main__":
    print("This is the main file")
    game = Game()
    game.play()