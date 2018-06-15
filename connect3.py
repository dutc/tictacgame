"""
Plays ConnectN?
"""

player_to_character = {
    None : ' ',
    1 : 'o',
    2 : 'x'
}

def play_game():
    b = Board()
    player = 1
    while not b.winner():
        b.render()
        move = input(f"Player {player}'s turn: ")
        column = int(move)
        b.play(column, player)
        if player == 1:
            player = 2
        else:
            player = 1
    b.render()

def print_label_row(width):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = alphabet[:width]
    for letter in letters:
        print(' ' + letter + ' ', end=' ')

    print()

def print_game_row(row):
    rendered_cols = [' ' + player_to_character[value] + ' ' for value in row]
    print('|'.join(rendered_cols))

def print_base_row(width):
    print('-' * 4 * width)


def find_winner_in_sequence(seq):
    current_run = None
    length = 0
    for s in seq:
        if not s:
            length = 0
            current_run = None
        else:
            if current_run == s:
                length += 1
            else: # Starting a new run with a different player
                current_run = s
                length = 1

            if length >= 3:
                return current_run # The winner, because they have more than 3 in a row!
    return None
        

class Board:
    def __init__(self, height=6, width=5):
        self.height = height
        self.width = width
        self.board = [[None] * width for _ in range(height)]

    def render(self):
        print_label_row(self.width)
        for row in self.board:
            print_game_row(row)
        print_base_row(self.width)
        self.print_if_victor()


    def print_if_victor(self):
        winner = self.winner()
        if winner:
            print(f"Player {winner} wins!")

    def play(self, column, player):
        """Plays a move in column where player is 1 or 2"""
        # 1. Find the first empty row in that column
        empty_row = None
        for row_number, row in enumerate(self.board):
            if row[column] is None:
                empty_row = row_number
            else:
                break

        # 2. Put the value in the right place
        self.board[empty_row][column] = player

    def get_col(self, col_num):
        """returns the data in a column (rows are trivial so we don't have a method for that)
        """
        return [row[col_num] for row in self.board]

    def get_diagonal_rightwards(self, row, column):
        """Gets diagonal data starting in the left and heading upwards to the right"""
        output = []
        r, c = row, column
        while c < self.width and r < self.height and c >= 0 and r >= 0:
            output.append(self.board[r][c]) 
            r -= 1
            c += 1
        return output

    def get_diagonal_leftwards(self, row, column):
        """Gets diagonal data starting in the right and heading upwards to the left"""
        output = []
        r, c = row, column
        while c < self.width and r < self.height and c >= 0 and r >= 0:
            output.append(self.board[r][c]) 
            r -= 1
            c -= 1
        return output
        
    def winner(self):
        """
        Returns None if nobody has won, or else the player number who is
        victorious
        """
        board = self.board
        for row in board:
            w = find_winner_in_sequence(row)
            if w:
                return w
            
        for col in range(self.width):
            w = find_winner_in_sequence(self.get_col(col))
            if w:
                return w

        for col in range(self.width):
            for row in range(self.height):
                l_diag = self.get_diagonal_leftwards(row, col)
                r_diag = self.get_diagonal_rightwards(row, col)
                w = find_winner_in_sequence(l_diag)
                if w:
                    return w
                w = find_winner_in_sequence(r_diag)
                if w:
                    return w
        return None

def test():
    b = Board()
    b.play(column=0, player=1)
    b.play(column=1, player=1)
    b.play(column=2, player=1)
    b.render()
    assert b.winner() == 1
    b = Board()
    b.play(column=0, player=1)
    b.play(column=0, player=1)
    b.play(column=0, player=1)
    b.render()
    assert b.winner() == 1

    b = Board()
    b.play(column=0, player=1)
    b.play(column=1, player=2)
    b.play(column=2, player=2)
    b.play(column=1, player=1)
    b.play(column=2, player=1)
    b.play(column=2, player=1)
    b.render()
    assert b.winner() == 1

play_game()
