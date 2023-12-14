# Refactored and Improved Code for Tic-Tac-Toe (XO) Game:

import random
import tkinter as tk
import re

# Initialize win counters
winCounterX = 0
winCounterO = 0

def xo(cellsList: tk.Button, cellIndex: int, turn: list, resultList: list, playerX: tk.Label, playerO: tk.Label, matchWinner: tk.Label):
    global winCounterX, winCounterO

    result = "X" if turn[0] % 2 == 0 else "O"
    turn[0] += 1

    # Update button state
    cellsList[cellIndex]["text"] = result
    cellsList[cellIndex]["command"] = lambda: None
    resultList[cellIndex] = result

    # Check for a win or tie
    toString = "".join(resultList)
    winState = checkWin(xoString=toString)

    if winState == "Tie":
        for i in range(9):
            cellsList[i]["bg"] = "crimson"
        matchWinner["text"] = "Tie, no one wins"
    elif winState:
        winner = checkWinner(cellsList, matchWinner, winState)
        if winner:
            if winner == "O":
                winCounterO += 1
                playerO["text"] = f"Computer: {winCounterO}"
            elif winner == "X":
                winCounterX += 1
                playerX["text"] = f"You: {winCounterX}"

            for cell in cellsList:
                cell["command"] = lambda: None

    # Computer's move (comment to disable computer player)
    randomIndex = random.randint(0, 8)
    if turn[0] % 2 == 1 and winState is None:
        while resultList[randomIndex] != ",":
            randomIndex = random.randint(0, 8)
        xo(cellsList, randomIndex, turn, resultList, playerX, playerO, matchWinner)

def checkWinner(cellsList, matchWinner, winState):
    theWinner = None

    for group_number in range(1, len(winState.groups()) + 1):
        if winState.start(group_number) != -1:
            matched_substring = winState.group(group_number)

            if matched_substring is not None and "X" in matched_substring.upper():
                theWinner = "X"
            elif matched_substring is not None and "O" in matched_substring.upper():
                theWinner = "O"

            start_winning_position = winState.start(group_number)
            end_winning_position = winState.end(group_number)

            if start_winning_position + 1 == end_winning_position:
                cellsList[start_winning_position]["bg"] = "cyan"
            else:
                i = start_winning_position
                while i < end_winning_position:
                    cellsList[i]["bg"] = "cyan"
                    i += 1

    if theWinner:
        matchWinner["text"] = f"{theWinner} wins"
    return theWinner

def resetter(cellsList, resultList, turnsCounterReset, playerX, playerO, matchWinnerReset):
    turnsCounterReset[0] = 0
    for Index in range(9):
        cellsList[Index]["text"] = " "
        cellsList[Index]["command"] = lambda i=Index: xo(cellsList, i, turnsCounterReset, resultList, playerX, playerO, matchWinnerReset)
        cellsList[Index]["bg"] = "white"
        resultList[Index] = ","
        matchWinnerReset["text"] = "    "

def checkWin(xoString: str):
    isThereSpace: bool = re.search(r",", xoString)
    diagonalPattern1 = "^..(x).(x).(x)|^..(o).(o).(o)"
    diagonalPattern2 = "(x)...(x)...(x)|(o)...(o)...(o)"
    rowPatterns = "(^XXX)|((?<=^.{3})XXX)|(XXX$)|(^OOO)|((?<=^.{3})OOO)|(OOO$)"
    columnPatterns = "(x)..(x)..(x)|(o)..(o)..(o)"
    winCasesPatternsFor = f"{diagonalPattern1}|{diagonalPattern2}|{rowPatterns}|{columnPatterns}"
    match = re.search(winCasesPatternsFor, xoString, re.IGNORECASE)

    if match:
        return match
    elif isThereSpace:
        return None
    else:
        return "Tie"



# Initialize turn counter and result list
turnCounter = [0]
xoResult = ["," for _ in range(9)]
buttons = [None for _ in range(9)]

# GUI Setup
window = tk.Tk()
window.title("Tic-Tac-Toe game")

# Labels for displaying results
frmResults = tk.Frame(master=window)
lblName = tk.Label(master=frmResults, text="You: 0", padx=5, relief="flat", font=("Sans-serif", 16))
lblComputer = tk.Label(master=frmResults, text="Computer: 0", padx=5, relief="flat", font=("Sans-serif", 16))
lblWinner = tk.Label(master=window, text="       ", padx=10, pady=10, relief="flat", font=("Sans-serif", 24))

lblName.pack(side="left")
lblComputer.pack(side="left")
frmResults.pack(anchor="n", padx=10, pady=10, expand=True)
lblWinner.pack()

# Button to restart the game
btnRestart = tk.Button(
    master=window, text="Restart", padx=5, pady=5, font=("Sans-serif", 16),
    command=lambda: resetter(buttons, xoResult, turnCounter, lblName, lblComputer, lblWinner)
)
btnRestart.pack(side="top")

# Game board setup
frmBoard = tk.Frame(master=window)
frmBoard.rowconfigure([0, 1, 2], weight=1, minsize=30)
frmBoard.columnconfigure([0, 1, 2], weight=1, minsize=30)
frmBoard.pack(padx=10, pady=10)

# Create buttons for the game board
for row in range(3):
    for column in range(3):
        Index = row * 3 + column
        btnCell = tk.Button(
            master=frmBoard, text=" ", border=1, width=2, height=2, relief="solid", font=("Sans-serif", 24),
            command=lambda i=Index: xo(buttons, i, turnCounter, xoResult, lblName, lblComputer, lblWinner)
        )
        btnCell.grid(column=column, row=row, ipadx=40, ipady=25)
        buttons[Index] = btnCell

# Run the GUI application
window.mainloop()
