from enum import Enum
from collections import deque

class PieceType(Enum):
    X = 1
    O = 2

class PlayingPiece:
    def __init__(self, pieceType):
        self.pieceType = pieceType

    def __str__(self):
        return "X" if self.pieceType == PieceType.X else "O"

class PieceX(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)

class PieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]
    
    def __str__(self):
        # print board with borders
        result = ""
        for i in range(self.size):
            for j in range(self.size):
                result += "  " if self.board[i][j] is None else " " + str(self.board[i][j])
                if j < self.size - 1:
                    result += " |"
            result += "\n"
            if i < self.size - 1:
                result += "-" * (self.size * 4 - 1) + "\n"
        return result
    
    def move(self, row, col, piece):
        if self.board[row][col] is not None:
            return False
        self.board[row][col] = piece
        return True

    def has_winner(self, piece):
        for i in range(self.size):
            # row
            if all(self.board[i][j] == piece for j in range(self.size)):
                return True
            # column
            if all(self.board[j][i] == piece for j in range(self.size)):
                return True
        # diagonal
        if all(self.board[i][i] == piece for i in range(self.size)):
            return True
        # anti-diagonal
        if all(self.board[i][self.size - i - 1] == piece for i in range(self.size)):
            return True
        return False

    def freecells(self):
        return [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] is None]

class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece
    
    def __str__(self):
        return self.name + " (" + str(self.piece) + ")"
    
    def get_name(self):
        return self.name
    
    def get_piece(self):
        return self.piece

class TicTacToe:
    def __init__(self):
        self.players = deque()
        self.board = None
        self.initiate_game()
    
    def initiate_game(self):
        self.players.append(Player("Player 1", PieceX()))
        self.players.append(Player("Player 2", PieceO()))
        self.board = Board(3)
    
    def start(self):
        nowinner = True
        while nowinner:
            player_turn = self.players.popleft()
            print(self.board)
            freespaces = self.board.freecells()
            if len(freespaces) == 0:
                nowinner = False
                return None
            
            print(player_turn.get_name() + " turn: " + "Enter row and column: ")
            row, col = map(int, input().split())

            if row < 0 or row >= self.board.size or col < 0 or col >= self.board.size:
                self.players.appendleft(player_turn)
                print("Invalid move, enter row and col in range 0 to " + str(self.board.size - 1))
                continue
                
            if not self.board.move(row, col, player_turn.get_piece()):
                self.players.appendleft(player_turn)
                print("Invalid move, cell already occupied")
                continue
                
            if self.board.has_winner(player_turn.get_piece()):
                nowinner = False
                return player_turn.get_name()
        
            self.players.append(player_turn)


if __name__ == "__main__":
    game = TicTacToe()
    winner = game.start()
    if winner:
        print("Winner: " + str(winner))
    else:
        print("It's a tie!")
