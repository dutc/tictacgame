
# must use is and not ==
nought = object()
cross = object()


#internal representation not display
def empty_board():
    array_size = [[None,None,None], [None,None,None], [None,None,None]]
    return array_size
    
def dash():
    print(11*'-')
def heading():
    print('   a   b   c') 


def print_row(number, row):
    print(str(number) + ' ', end = '')
    print_symbol(row[0])
    print('|', end = '')
    print_symbol(row[1])
    print('|', end = '')
    print_symbol(row[2])
  
 

#normally explicitly check values 
def print_symbol(a):
    if a is None:
        print('   ', end = '')
    elif a is nought:
        print(' 0 ', end = '')
    else:    
        print(' X ', end = '')

board = empty_board()


#arguments deifned when we call it 
def print_board(board):
    heading()
    print_row(1, board[1])
    dash()
    print_row(2, board[2])
    dash()
    print_row(3, board[3])

print("Please specify where you want to place your " + Value)
def user_input():
    if






    
