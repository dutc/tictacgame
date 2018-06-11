# Introduction

The following are instructions for a collaborative, team-based coding game.

It will be played at NYC Python on June 14, 2018: https://www.meetup.com/nycpython/events/

# Agenda

|    time     |     activity    |
|-------------|-----------------|
| 6:00 - 6:15 |     Setup       |
| 6:15 - 6:30 | Find Your Group |
| 6:30 - 7:00 |   Sprint #1     |
| 7:00 - 7:15 | Q&A Session #1  |
| 7:15 - 7:45 |   Sprint #2     |
| 7:45 - 8:00 | Q&A Session #2  |
| 8:00 - 8:30 |   Final Sprint  |
| 8:30        | Closing Notes   |

# Overview

Your tasks are as follows:
- create a command-line program, `tictacgame.py` that allows a user to
  interactively play a game of Tic Tac Toe
- create a command-line program, `connect3game.py` that allows a user to
  interactively play a game of Connect Three

# Specification: Tic Tac Toe

`tictacgame.py` should be a Python command-line script. It takes only one of two flags:
- `tictacgame.py -o`: user plays as the Os
- `tictacgame.py -x`: user plays as the Xs

The Xs move first.

The program should prompt the user for their move. The user can input their move
using a coordinate system (e.g., A1, B2, C1, etc.) as show below.

Then the game should choose a move. *NOTE: In the initial version, the opponent
should choose a random square. The opponent's moves do not need to be
strategic.*

The game should continue until one player wins.

```
$ python tictacgame.py -x

Let's Play!
You're Xs, I'm Os!

   a   b   c
1    |   |
  -----------
2    |   |
  -----------
3    |   |

Your move: b2
My move: a1

   a   b   c
1  o |   |
  -----------
2    | x |
  -----------
3    |   |

Your move: _
```

# Specification: Connect 3

`connect3game.py` should be a Python command-line script. It takes only one of two flags:
- `connect3game.py -o`: user plays as the Os
- `connect3game.py -x`: user plays as the Xs

You can choose how large of a game board to make. As a simplification, start
with a relatively small game board (as in the example below.)

```
$ python connect3game.py -x

Let's Play!
You're Xs, I'm Os!

  a   b   c   d   e
    |   |   |   |   
    |   |   |   |
    |   |   |   |
    |   |   |   |   
    |   |   |   |
    |   |   |   |
--------------------

Your move: b
My move: a

  a   b   c   d   e
    |   |   |   |   
    |   |   |   |
    |   |   |   |
    |   |   |   |   
    |   |   |   |
  o | x |   |   |
--------------------

Your move: b
My move: c

  a   b   c   d   e
    |   |   |   |   
    |   |   |   |
    |   |   |   |
    |   |   |   |   
    | x |   |   |
  o | x | o |   |
--------------------

Your move: _
```

# 6:00 - 6:15 Getting Started

You will need the following prerequisites to play.
Please notify an organizer if you need help with any of the following.

1. a team (we'll help you find a group)
2. a Github account (we'll help you create one)
3. Python\* installed on your computer (we can help you install Python)

\* You should be able to write this game without needing anything other than
   the standard Python, as downloaded from http://python.org or
   https://www.anaconda.com/download.
   You will not need any third-party libraries or any special tools to complete
   these exercises.

# 6:30 - 7:15 Sprint #1 Recommendation

Focus on `tictacgame.py`.

# 7:15 - 7:45 Sprint #2 Recommendation
# 8:00 - 8:30 Sprint #3 Recommendation
