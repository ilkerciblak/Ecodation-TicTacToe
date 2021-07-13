
# Importing the relevant and required libraries
from random import randint
import os
# Required Functions

# Func1 → Displaying the Game Board

def DisplayBoard(board):
    os.system('cls')
    '''
    Function accepts game board as an input
    and ONLY displays it, returns nothing.
    '''
    a = '+' + '-'*7 # +-----+ padding
    b = '|' + ' '*7 # |    | padding

    for row in range(3):

        print(a*3, end = '+\n')

        for column in range(3):
            if column == 1:
                print(*[f"|{num:^7}" for num in board[row]],sep="", end="|\n")

            else:
                print(b * 3, end='|\n')
    print(a*3, end = '+\n')

# Func2 → Function accepts move placement

def EnterMove():

    global gameBoard

    #print(gameBoard)
    ok = False
    while not ok:

        move = int(input("Lütfen Kare Seçin [1-9]: "))
        ok = move in list(range(1,10))  # kullanıcı girişi doğru aralıkta mı?
        if not ok:
            print("[1-9] Arası Kare Seçmediniz. Lütfen Tekrar Giriniz!")
            continue
        while True:
            try:
                move = dict( (j,(x, y)) for x, i in enumerate(gameBoard) for y, j in enumerate(i) )[move] 	# bu üç satır çok önemli. seçili digit değerine sahip kareyi
                break
            except:
                move = int(input("Dolu Bir Kare Seçtiniz: Lütfen Kare Seçin [1-9]: "))
                continue

        row = move[0] 	# [row][col] değerine dönüştürmeliyiz. Örn
        col = move[1]		# 1 → [0][0], 2 → [0][1], 3 → [0][2], 4 → [1][0], 6 → [1][2] gibi
        sign = gameBoard[row][col]  # seçili kareyi oku
        ok = sign not in ['O', 'X']
        if not ok:  # seçili kare dolu ise tekrar denenmeli
            print("Seçili Kare. Lütfen Tekrar Giriniz!")
            continue
        gameBoard[row][col] = 'O'    	# seçili kareyi '0' olarak set et




def VictoryFor(board, mark):
    players = {'O':'Oyuncu', 'X':'Bilgisayar'}

    if (board[0][0] == board[1][1] == board[2][2] == mark
    or board[0][2] == board[1][1] == board[2][0] == mark):
        winner = players[mark]
        return winner

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][-1] == mark: # checking the rows
            winner = players[mark]
            break
        elif board[0][i] == board[1][i] == board[2][i] == mark: # cheking the columns
            winner = players[mark]
            break
    else:

        winner = None

    return winner



def MakeListOfFreeFields(board):
    free = list()
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free

def DrawMove():
    global gameBoard
    free = MakeListOfFreeFields(gameBoard)  # boş olan karelerden bir liste tanımlayalım
    cnt = len(free)
    if cnt > 0:  # list boş değil ise, 'X' i set edeceğimiz kareyi random seçelim
        correct = False
        while not correct:
            row, col = randint(0,2), randint(0,2)
            correct = (row, col) in free
        gameBoard[row][col] = 'X'

if __name__ == "__main__":
    gamePlay = True
    while gamePlay:
        # Creating the board list which contains inputs and empty spaces
        gameBoard = [[3*i+j+1 for j in range(3)] for i in range(3)] # Places assigned w/ integers in order to ease the usage
        gameBoard[1][1] = 'X' # Pre-set of the '5' numbered place



        humanTurn = gamePlay = True # Letting the player to do second move and let the game begin

        # GamePlay
        while True:

            DisplayBoard(gameBoard)

            if humanTurn:
                #try:
                EnterMove() # User selects a place to sign
                victory = VictoryFor(gameBoard, 'O') # Checking if the player wins
                humanTurn = not humanTurn
                #except:
                    #print('Something Wrong in humanTurn')
            else:
        #        try:
                DrawMove()
                victory = VictoryFor(gameBoard, 'X') # Checking if the computer wins
                humanTurn = not humanTurn
        #        except:
        #        print('Something Wrong in ComputerTurn')
            freePlaces = MakeListOfFreeFields(gameBoard) # list of free places

    # Altering the Turn by means of using Human Turn variable



    # Checking if there is a winner or any empty space left

            if victory != None or len(freePlaces) == 0:
                DisplayBoard(gameBoard)

                if victory is None and len(freePlaces) == 0:
                    try:
                        print(f'Oyun Berabere Tamamlandı!')
                        gamePlay = input('Tekrar oynamak ister misin ?                   Y-y/N-n:').lower() == 'y'
                        break
                    except:
                        print('Something wrong in Tied option')
                elif victory != None:

                        print(f'Oyun Bitti! Kazanan : {victory}')
                        gamePlay = input('Tekrar oynamak ister misin ?                   Y-y/N-n:').lower() == 'y'
                        break


    # If there is a winner or no empty space, game is going to be intrupped and result will be shown
