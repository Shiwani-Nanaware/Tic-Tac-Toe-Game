#Tic Tac Toe Game
from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="---Tic Tac Toe---",font=("Arial",30),bg="skyblue")
titleLabel.grid(row=0,column=1)

frame2 = Frame(root)
frame2.pack()

board = { 1:" ",2:" ",3:" ",
          4:" ",5:" ",6:" ",
          7:" ",8:" ",9:" "}  #dictionary to track status of buttons

turn = "X" #initialize variable turn to X
game_end = False 

#function to check winner
def checkForWin(player):
    if board[1] == board[2] == board[3] and board[3] == player: #condition for 1st row
        return True
    elif board[4] == board[5] == board[6] and board[6] == player: #condition for 2nd row
        return True
    elif board[7] == board[8] == board[9] and board[9] == player: #condition for 3rd row
        return True
    elif board[1] == board[4] == board[7] and board[7] == player: #condition for 1st col
        return True
    elif board[2] == board[5] == board[8] and board[8] == player: #condition for 2nd col
        return True
    elif board[3] == board[6] == board[9] and board[9] == player: #condition for 3rd col
        return True
    elif board[1] == board[5] == board[9] and board[9] == player: #condition for diagonal
        return True
    elif board[3] == board[5] == board[7] and board[7] == player: #condition for diagonal
        return True

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"]= " "
    for i in board.keys():
        board[i] = " "
    winningLabel = Label(frame1,text=f" ",font=("Arial",30),width=25)
    winningLabel.grid(row = 3, column = 0, columnspan = 3)

#function to play
def play(event):
    global turn,game_end
    if game_end:
        return
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    #print(clicked)
    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)
    
    if button["text"]==" ":
        if turn == "X":
            button["text"]="X"
            board[clicked]=turn
            if checkForWin(turn):
                winningLabel = Label(frame1,text=f"Player {turn} wins the Game",font=("Arial",30),bg="orange",width=20)
                winningLabel.grid(row = 3, column = 0, columnspan = 3)
                game_end = True
            turn = "O"
        else:
            button["text"]="O"
            board[clicked]=turn
            if checkForWin(turn):
                winningLabel = Label(frame1,text=f"Player {turn} wins the Game",font=("Arial",30),bg="orange",width=20)
                winningLabel.grid(row = 3, column = 0, columnspan = 3)
                game_end = True
            turn = "X"
        if checkForDraw():
            gameDrawLabel = Label(frame1,text=f" Game Draw ! ! !",font=("Arial",30),bg="red",width=20)
            gameDrawLabel.grid(row = 3, column = 0, columnspan = 3)

    

#tic tac toe board
#1st row
button1 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button2 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button2.grid(row=0,column=1)
button2.bind("<Button-1>",play)

button3 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button3.grid(row=0,column=2)
button3.bind("<Button-1>",play)

#2nd row
button4 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button4.grid(row=1,column=0)
button4.bind("<Button-1>",play)

button5 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button5.grid(row=1,column=1)
button5.bind("<Button-1>",play)

button6 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button6.grid(row=1,column=2)
button6.bind("<Button-1>",play)

#3rd row
button7 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button7.grid(row=3,column=0)
button7.bind("<Button-1>",play)

button8 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button8.grid(row=3,column=1)
button8.bind("<Button-1>",play)

button9 = Button(frame2,text=" ",width=4,height=2,font=("Arial",35),borderwidth=5)
button9.grid(row=3,column=2)
button9.bind("<Button-1>",play)

restartButton = Button(frame2,text="Restart GAME",width=12,height=1,font=("Arial",20),bg="lightgreen",relief=RAISED,borderwidth=2,command=restartGame)
restartButton.grid(row=4,column=0,columnspan=5)

buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9] #for use in restart function
root.mainloop() #to stay board on screen