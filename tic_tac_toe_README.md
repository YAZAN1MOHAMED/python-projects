# Tic-Tac-Toe (XO) Game

## Overview

This is a simple implementation of the classic Tic-Tac-Toe (XO) game using Python and the Tkinter library for the graphical user interface. The game supports a two-player mode, where the players take turns to mark their symbols on a 3x3 grid. Additionally, there's an optional computer player that makes random moves.

## Table of Contents
1. [Features](#features)
2. [How to Play](#how-to-play)
3. [Code Structure](#code-structure)
    - [UI Generation](#ui-generation)
    - [Function Implementation](#function-implementation)
    - [Regex and Game Logic](#regex-and-game-logic)
4. [Contributing](#contributing)
5. [License](#license)

## Features

- Two-player mode with UI interactions.
- Optional computer player with random moves.
- Win and tie detection with highlighted winning cells.

## Getting Started
Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](python.org).

##Installation
1\ Clone the repository:
```
git clone https://github.com/YAZAN1MOHAMED
/python-projects/tic_tac_toe_game.git
```

2\ Change directory to the project folder:

`cd tic-tac-toe`

3\ Run the game:

`python xo_game.py`

## How to Play

1. **Run the Game:**
   - Execute the code, and the game window will appear.

2. **Player Moves:**
   - Click on any empty cell to make a move.
   - The game alternates between "X" and "O" symbols.

3. **Win or Tie:**
   - The game detects a win or tie and updates the UI accordingly.
   - Winning cells are highlighted, and win counters are updated.

4. **Restart:**
   - Click the "Restart" button to reset the game.

## Code Structure

### UI Generation

- The Tkinter library is used for GUI setup.
- Labels display player scores and the game winner.
- Buttons represent cells on the game board.

### Function Implementation

- `xo` function handles player and computer moves.
- `checkWinner` identifies the winner based on the current board state.
- `resetter` resets the game board and counters.

### Regex and Game Logic

- Regular expressions are employed to check for win patterns.
- `checkWin` uses regex to identify winning patterns (rows, columns, and diagonals).
- The game logic handles player moves, computer moves (optional), and win/tie detection.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for improvements.


