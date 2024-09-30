import random
from collections import deque

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

class Dice:
    def __init__(self, diceCount):
        self.diceCount = diceCount
        self.minValue = 1
        self.maxValue = 6
    
    def roll(self):
        return sum(random.randint(self.minValue, self.maxValue) for _ in range(self.diceCount))

class Jump:
    '''
    Jump class represents a snake or a ladder.
    Snake goes down from start to end.
    Ladder goes up from start to end
    '''
    def __init__(self):
        self.start = None
        self.end = None

    def __str__(self):
        return str(self.start) + " -> " + str(self.end)

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_start(self, start):
        self.start = start
    
    def set_end(self, end):
        self.end = end
    
    def __str__(self):
        res = ""
        if self.start > self.end:
            res += "Snake: "
        else:
            res += "Ladder: "
        res += str(self.start) + " -> " + str(self.end)
        return res

class Cell:
    def __init__(self):
        self.jumps = None

class Board:
    def __init__(self, size, numSnakes, numLadders):
        self.size = size
        self.board = [Cell() for _ in range(size * size)]
        self.numSnakes = numSnakes
        self.numLadders = numLadders
        self.add_jumps()
    
    def add_jumps(self):
        curr_snakes, curr_ladders = 0, 0
        
        while curr_snakes < self.numSnakes:
            start = random.randint(11, self.size * self.size - 2)
            end = random.randint(0, start - 10)
            if self.board[start].jumps is None and self.board[end].jumps is None:
                snake = Jump()
                snake.set_start(start)
                snake.set_end(end)
                self.board[start].jumps = snake
                curr_snakes += 1
        
        while curr_ladders < self.numLadders:
            start = random.randint(0, self.size * self.size - 12)
            end = random.randint(start + 10, self.size * self.size - 1)
            if self.board[start].jumps is None and self.board[end].jumps is None:
                ladder = Jump()
                ladder.set_start(start)
                ladder.set_end(end)
                self.board[start].jumps = ladder
                curr_ladders += 1
    
    def __str__(self):
        res = ""
        # return snakes and ladders start and end positions
        for cell in self.board:
            if cell.jumps is not None:
                res += str(cell.jumps) + "\n"
        return res

class SnakeAndLadder:
    def __init__(self):
        self.board = None
        self.dice = None
        self.players = deque()
        self.winner = None
        self.initiate_game()
    
    def initiate_game(self):
        self.board = Board(10, 5, 5)
        self.dice = Dice(1)
        self.add_players()
    
    def add_players(self):
        self.players.append(Player("Player 1"))
        self.players.append(Player("Player 2"))
    
    def get_player_turn(self):
        player = self.players.popleft()
        self.players.append(player)
        return player
    
    def start(self):
        print(self.board)
        while not self.winner:
            player = self.get_player_turn()
            print("Player " + player.get_name() + " turn" + "position: " + str(player.get_position()))

            diceValue = self.dice.roll()
            print("Dice Value: " + str(diceValue))

            if player.get_position() + diceValue == self.board.size * self.board.size:
                player.set_position(player.get_position() + diceValue)
                self.winner = player
            elif player.get_position() + diceValue < self.board.size * self.board.size:
                player.set_position(player.get_position() + diceValue)
                if self.board.board[player.get_position()].jumps is not None:
                    jump = self.board.board[player.get_position()].jumps
                    if jump.get_start() > jump.get_end():
                        print("Oops! Snake")
                    else:
                        print("Yay! Ladder")
                    player.set_position(jump.get_end())
                    

if __name__ == '__main__':
    game = SnakeAndLadder()
    game.start()
    print("Game Over. Winner is " + str(game.winner))