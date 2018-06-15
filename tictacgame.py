import numpy as np
import sys
import random
from itertools import product

human = sys.argv[1][-1]
computer = 'o' if human == 'x' else 'x'

def stringify(board):
    return '\n-----\n'.join(map(lambda y: '|'.join(y), [map(lambda x: ' ' if x == '' else x, list(sublist)) for sublist in board]))

board = np.chararray((3,3))
board[:] = ' '

cache = list(product(range(3), repeat=2))

print("Let's Play!")
if computer == 'x':
    print("You're Os, I'm Xs!")
    m , n = random.choice(cache)
    board[m,n] = 'x'
    cache.remove((m,n))
else:
    print("You're Xs, I'm Os!")

print(stringify(board))
user_input = raw_input("Insert coordinate: ")

try:
    convert = dict([(y,x) for x, y in enumerate(['A','B','C'])])
    for value in range(3):
        convert[str(value)] = value
    coord = tuple(map(lambda x: convert[x], list(user_input)))

    if coord in cache:
        board[coord] = human
        cache.remove(coord)
    else:
        print("Position already taken. Please try again.")
except KeyError:
    print("Invalid Entry. Try again.")
