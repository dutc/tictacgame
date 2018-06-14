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

The elements to make tictacgame work are:

* The board
* Displaying game state
* A move interface
* Player input
* AI strategy
* AI input
* Checking for victory
* the engine

## The Board

Tic-Tac-Toe is small enough that the in memory representation can be
almost anything. Whoever takes on the board should also consider
how to display it.

Remember that this object (whatever it is) will need to talk to your
teammate's systems, and you'll need to formalize the API for
interacting with it very quickly.

## Player Input

This is a somewhat simple problem with a few tricks. Remember that
ultimately what the player inputs does not need to match how your team
represents that information in the system. Also consider what you do if
your player provides inappropriate input.

You'll also need to set up the command line interface to run your
script.

## The Move Interface

The move interface is how player and AI input can translate input into
updating the game state.

You probably don't want the API to match how users will input their
moves.

This will either need to be a function that takes a board object _or_ a
method on a `Board` class. (Or maybe there's a third way.)

## AI

This is the hard part.

Consider that the move decision is based on a series of binary choices.

Recognize that the AI will need to be told it's time to move.

The API between the AI and the Move Interface is going to be important.
(Consider firming up how this happens in the first few minutes.)

## Checking For Victory

You have a board, you have moves that are stored how you like, now, at
the end of each turn, you need to check for victory.

Write an algorithm that can check the board for possible wins.

This absolutely needs either a well defined board interface _or_ a
completed board to be able to build.

## The engine

This is the glue code that keeps the loop running. Can be written first,
it can be written as you go and have new features available, or it can
be written last, once all the features work.

# 7:15 - 7:45 Sprint #2 Recommendation

During this period you should finish tic-tac-toe if you haven't, but
at some point, you should start connect 3.

Connect3 is remarkably similar to Tic Tac Toe but to cover the bases,
you'll need:

* A board
* A move interface
* Player input
* AI input
* AI decision making
* Checking for victory
* An engine

The good news is, your engine from Tic-Tac-Toe can probably run
connect3 without too much modification.

## The Board

Your board is different, as are your moves. Whatever representation you
built before, it can likely be modified to fit the new board style.

## The Move Interface

## Player Input

## AI

AI for connect 3 is going to be more complicated than Tic-Tac-Toe, so
focus on connecting to the move interface. After you do that,
implment a random choice methodology that can be used for a fallback.

After that, it's all about choosing what decisions to prioritize and
writing code that lets you add new decisions (in arbitrary orders) as
you go. Expect to need your entire team to get this running well.

## Check for Victory

# 8:00 - 8:30 Sprint #3 Recommendation

## AI