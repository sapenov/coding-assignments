import random

class Game:

    def __init__(self, start_player, board_size):
        self.board = Board(board_size)
        self.player = start_player
        self.game_id = 0
        self.rounds_left = board_size * board_size
        self.game_over = False

    def play(self):
        # begins new game and assigns new game id
        self.game_id = random.random()
        print("Welcome to the game # {}".format(self.game_id))

        while not self.game_over:
            self.print_current_player_turn()
            row_col = input('Player make your move [row col]: ')
            row, col = self.get_row_col(row_col)
            self.play_round(row, col)

    def play_round(self, row, col):
        # executes a single round of the game by
        # placing a piece at the position of row, col.
        if self.board.can_place_piece(row, col):
            self.board.place_piece(row, col, self.player)
            self.print_current_move(row, col)
            self.board.print_board()

            if self.board.check_win_condition(self.player):
                self.declare_winner(self.player)
                return

            self.decrement_rounds()
            if self.rounds_left == 0:
                self.declare_tie()
                return

            self.switch_player()
        else:
            # using helper method to print invalid move
            self.print_invalid_move(row, col)

    def get_row_col(self, input_string):
        if input_string:
            parts = input_string.strip().split(' ')
            if len(parts) < 2:
                print('Invalid inputs!! Enter row and col indices')
                return -1, -1
            else:
                return int(parts[0]), int(parts[1])

    def print_current_player_turn(self):
        print('It is {}\'s turn'.format(self.player))

    def decrement_rounds(self):
        # reduces the number of rounds remaining.
        self.rounds_left -= 1

    def declare_winner(self, player):
        # declares the given player as the winner
        self.game_over = True
        print('Player {} is the winner!'.format(self.player))

    def declare_tie(self):
        # declares a tie
        self.game_over = True
        print('Game {} is a tie!'.format(self.game_id))

    def print_invalid_move(self, row, col):
        # declares a move invalid
        print('Invalid move placing {} at {} {}'.format(self.player, row, col))

    def print_current_move(self, row, col):
        # prints the move just made
        print('{} was placed at {} {}'.format(self.player, row, col))

    def switch_player(self):
        # changes current player.
        if self.player.lower() == 'x':
            self.player = 'O'
        else:
            self.player = 'X'


class Board:

    def __init__(self, dim):
        self.dim = dim
        self.empty_char = '.'
        self.matrix = [[self.empty_char for i in range(self.dim)] for j in range(self.dim)]

    def print_board(self):
        # print current state of the board
        for i in range(self.dim):
            row = " | ".join(x for x in self.matrix[i])
            print(row)

    def can_place_piece(self, row, col):
        if 0 <= row < self.dim and 0 <= col < self.dim:
            return self.matrix[row][col] == self.empty_char
        else:
            return False

    def place_piece(self,row, col, player):
        self.matrix[row][col] = player

    def check_diagonals(self, player):
        for i in range(self.dim):
            if self.matrix[i][i] != player:
                return False

    def check_rows(self, player):
        winning_row = False
        for i in range(self.dim):
            winning_row = True
            for j in range(self.dim):
                if self.matrix[i][j] !=player:
                    winning_row = False
                    break
            if winning_row:
                return winning_row
        return winning_row

    def check_columns(self, player):
        winning_column = False
        i, j = 0,0
        while i < self.dim:
            winning_column = True
            while j < self.dim:
                if self.matrix[j][i] !=player:
                    winning_column = False
                    break
                j+=1
            i+=1

            if winning_column:
                return winning_column
        return winning_column

    def check_win_condition(self, player):
        return (self.check_columns(player) or self.check_diagonals(player)
                or self.check_rows(player))


g = Game("X", 3)
g.play()

# testing
# b = Board(3)
# b.print_board()
# print("New move...")

# # No winner moves:
# b.place_piece(0,0,'X')
# b.place_piece(0,1,'X')
# b.place_piece(1,2,'X')

# # Winning moves:
# # b.place_piece(0,0,'X')
# # b.place_piece(1,0,'X')
# # b.place_piece(2,0,'X')

# # print(b._check_diagonals('X'))
# # print(b._check_rows('X'))
# # print(b._check_columns('X'))
# print(b.check_win_condition('X'))
# b.can_place_piece(1,1)
# b.print_board()

