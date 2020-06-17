# minesweeper

class Game:
    def __init__(self, players, bs):
        self.board = Board(bs)
        self.game_over = False
        self.player = players[0]

    def play(self):
        print("Welcome to the Minesweeper game! \n "
              "Please read rules here. \n "
              "Starting the game...\n")
        while not self.game_over:
            self.print_current_players_turn()
            row_col = input("Player {}, please make your move, in 'row col' format like '1 2': ".format(self.player))
            r, c = self.get_move(row_col)
            self.play_round(r, c)



    def play_round(self, row, col):
        if self.board.is_valid_move(row, col):
            self.board.mark_cell_opened(row, col, self.player)
            self.print_current_move(row, col)
            self.board.print_board()
        else:
            self.print_invalid_move(row, col)

    def get_move(self, input_string):
        if input_string:
            parts = input_string.strip().split(' ')
            if len(parts) < 2:
                print('Invalid inputs!! Enter row and col indices')
                return -1, -1
            else:
                return int(parts[0]), int(parts[1])

    def print_current_players_turn(self):
        print("It is now turn of player {}".format(self.player))

    def print_invalid_move(self, row, col):
        # declares a move invalid
        print('Invalid move placing {} at {} {}'.format(self.player, row, col))

    def print_current_move(self, row, col):
        # prints the move just made
        print('{} was placed at {} {}'.format(self.player, row, col))

    def switch_player(self):
        pass


class Board:
    def __init__(self, dim):
        self.dim = dim
        self.empty_cell = '[]'
        self.matrix = [[self.empty_cell for i in range(self.dim)] for j in range(self.dim)]

    def print_board(self):
        for i in range(self.dim):
            row = " | ".join(x for x in self.matrix[i])
            print(row)

    def is_valid_move(self, row, col):
        if 0 <= row < self.dim and 0<= col < self.dim:
            # can be opened
            return self.matrix[row][col] == self.empty_cell
        else:
            return False

    def mark_cell_opened(self, row, col, player):
        self.matrix[row][col] = player

    def check_win_condition(self):
        pass

    def check_mine_explosion(self):
        pass

# initiate the game with following parameters
# board size
# number of mines
board_size = 6
players = ['A', 'B']
g = Game(players, board_size)
g.play()
