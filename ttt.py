
class Game:

    def __init__(self):
        pass

    def play(self):
        pass

    def play_round(self):
        pass

    def print_current_player_turn(self):
        pass

    def decrement_rounds(self):
        pass

    def declare_winner(self):
        pass

    def declare_tie(self):
        pass

    def print_invalid_move(self):
        pass

    def print_current_move(self, row, col):
        pass

    def switch_player(self):
        pass


class Board:

    def __init__(self, dim):
        self.dim = dim
        self.empty_char = '.'
        self.matrix = [[self.empty_char for i in range(self.dim)] for j in range(self.dim)]

    def print_board(self):
        pass

    def can_place_piece(self, row, col):
        pass

    def place_piece(self,row, col, player):
        pass

    def check_win_condition(self, player):
        pass

    def check_diagonals(self, player):
        pass

    def check_rows(self, player):
        pass

    def check_columns(self, player):
        pass


g = Game()
g.play()

"""
b = Board(3)
b.print_board()
"""



