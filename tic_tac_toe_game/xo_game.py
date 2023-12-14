import random, tkinter as tk, re

winCounterX=0
winCounterO=0


def xo(cellsList: tk.Button, cellIndex: int, turn: list, resultList: list,playerX:tk.Label,playerO:tk.Label,matchWinner:tk.Label,):
    global winCounterX,winCounterO

    if turn[0] % 2 == 0:
        result = "X"
    else:
        result ="O"

    turn[0]+=1
    cellsList[cellIndex]["text"] = result
    cellsList[cellIndex]["command"] = lambda: None
    resultList[cellIndex] = result
    
    toString="".join(resultList)
    winState=checkWin(xoString=toString)
    if winState=="Tie":
        for i in range(9):
            cellsList[i]["bg"]="crimson"
        matchWinner["text"]="Tie no one win"
    elif winState:
        winner = checkWinner(cellsList, matchWinner, winState)
        if winner:
            if winner == "O":
                winCounterO+=1
                playerO["text"]=f"computer {winCounterO}"
            if winner == "X":
                winCounterX+=1
                playerX["text"]=f"You: {winCounterX}"
            for cell in cellsList:
                cell["command"] = lambda: None
    
    randomIndex=random.randint(0,8)
#comment these lines below to turn of computer
    if turn[0]%2==1 and winState==None:
        while resultList[randomIndex]!=",":
            randomIndex=random.randint(0,8)
        xo(cellsList,randomIndex,turn,resultList,playerX,playerO,matchWinner)


def checkWinner(cellsList, matchWinner, winState):#output the winner when x or o wins
    theWinner = None

    for group_number in range(1, len(winState.groups()) + 1):
        if winState.start(group_number) != -1:
            matched_substring = winState.group(group_number)

            if matched_substring is not None and ("X" in matched_substring.upper()):
                theWinner = "X"
            elif matched_substring is not None and ("O" in matched_substring.upper()):
                theWinner = "O"

            start_winning_position = winState.start(group_number)#take the position of the groups to change there color
            end_winning_position = winState.end(group_number)

            if start_winning_position + 1 == end_winning_position:
                cellsList[start_winning_position]["bg"] = "cyan"
            else:#to be able to change the color of xxx or ooo patterns
                i = start_winning_position
                while i < end_winning_position:
                    cellsList[i]["bg"] = "cyan"
                    i += 1
    if theWinner:
        matchWinner["text"] = f"{theWinner} wins"
    
    return theWinner

def resetter(cellsList,resultList,turnsCounterReset,playerX,playerO,matchWinnerReset):
    turnsCounterReset[0] = 0
    for Index in range(9):
        cellsList[Index]["text"] = " "
        cellsList[Index]["command"] = lambda i=Index: xo(
            cellsList, i, turnsCounterReset, resultList,playerX,playerO,matchWinnerReset
        )
        cellsList[Index]["bg"]="white"
        resultList[Index]=","
        matchWinnerReset["text"]="    "

def checkWin(xoString:str):
    isThereSpace:bool=re.search(r",",xoString)
    diagonalPattern1 = "^.{2}(x).(x).(x)|^.{2}(o).(o).(o)"
    diagonalPattern2="(x)...(x)...(x)|(o)...(o)...(o)"#Old pattern:(?<=.{2})X(?=.X.X)
    rowPatterns="(^XXX)|((?<=^.{3})XXX)|(XXX$)|(^OOO)|((?<=^.{3})OOO)|(OOO$)"
    columnPatterns="(x)..(x)..(x)|(o)..(o)..(o)"
    winCasesPatternsFor=f"{diagonalPattern1}|{diagonalPattern2}|{rowPatterns}|{columnPatterns}"
    match=re.search(winCasesPatternsFor , xoString,re.IGNORECASE)
    if match:return match
    elif isThereSpace:return None
    else: return "Tie"



#==========================================================================================
turnCounter = [0]  # list variable so that I can mutate it every time a button pressed
xoResult = ["," for _ in range(9)]
buttons = [None for _ in range(9)]


window = tk.Tk()
window.title("Tic-Tac-Toe game")
frm_results = tk.Frame(master=window)

lbl_name = tk.Label(master=frm_results,text="you: 0",padx=5,relief="flat",font=("Sans-serif",16,),
)
lbl_computer = tk.Label(master=frm_results,text="computer: 0",padx=5,relief="flat",font=("Sans-serif",16,),
)
lbl_winner = tk.Label(master=window,text="       ",padx=10,pady=10,relief="flat",font=("Sans-serif", 24),
)

lbl_name.pack(side="left")
lbl_computer.pack(side="left")
frm_results.pack(anchor="n",padx=10,pady=10,expand=True,
)
lbl_winner.pack()

btn_restart = tk.Button(
    master=window,text="Restart",padx=5,pady=5,font=("Sans-serif", 16),command=lambda: resetter(buttons,xoResult,turnCounter,lbl_name,lbl_computer,lbl_winner),
)
btn_restart.pack(side="top")

frm_board = tk.Frame(master=window)
frm_board.rowconfigure([0, 1, 2], weight=1, minsize=30)
frm_board.columnconfigure([0, 1, 2], weight=1, minsize=30)

frm_board.pack(padx=10, pady=10)

for row in range(3):
    for column in range(3):
        Index = row * 3 + column
        btn_cell = tk.Button(
            master=frm_board,
            text=" ",
            border=1,
            width=2,
            height=2,
            relief="solid",
            font=("Sans-serif", 24),
            command=lambda i=Index: xo(buttons, i, turnCounter, xoResult,lbl_name,lbl_computer,lbl_winner),
        )
        btn_cell.grid(
            column=column,
            row=row,
            ipadx=40,
            ipady=25,
        )
        buttons[Index] = btn_cell

window.mainloop()

