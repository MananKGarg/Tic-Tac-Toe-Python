#!usr/bin/env python3

def printBoard(board):
    print(' ' + board['1'] + ' ' + '|' + ' ' + board['2'] + ' ' + '|' + ' ' + board['3'] + ' ')
    print('-----------')
    print(' ' + board['4'] + ' ' + '|' + ' ' + board['5'] + ' ' + '|' + ' ' + board['6'] + ' ')
    print('-----------')
    print(' ' + board['7'] + ' ' + '|' + ' ' + board['8'] + ' ' + '|' + ' ' + board['9'] + ' ')


def checkWinner(board, turn):
    # 8 possible cases of victory

    if (board['1'] == board['2'] == board['3']) and (board['1'] != ' '):  # Top across
        printBoard(board)
        print()
        print('Game Over\n')
        print("***** " + turn + ' won, Congratulations.*****')
        return True
    elif (board['4'] == board['5'] == board['6']) and (board['4'] != ' '):  # Middle across
        printBoard(board)
        print()
        print('Game Over\n')
        print("***** " + turn + ' won, Congratulations.*****')
        return True
    elif (board['7'] == board['8'] == board['9']) and (board['7'] != ' '):  # Bottom across
        printBoard(board)
        print()
        print('Game Over\n')
        print("***** " + turn + ' won, Congratulations.*****')
        return True
    elif (board['1'] == board['4'] == board['7']) and (board['1'] != ' '):  # Left down
        printBoard(board)
        print()
        print('Game Over\n')
        print("***** " + turn + ' won, Congratulations.*****')
        return True
    elif (board['2'] == board['5'] == board['8']) and (board['2'] != ' '):  # Middle down
        printBoard(board)
        print()
        print('Game Over\n')
        print("***** " + turn + ' won, Congratulations.*****')
        return True
    elif (board['3'] == board['6'] == board['9']) and (board['3'] != ' '):  # Right down
        printBoard(board)
        print()
        print('Game Over\n')
        print("***** " + turn + ' won, Congratulations.*****')
        return True
    elif (board['1'] == board['5'] == board['9']) and (board['1'] != ' '):  # Diagonal left-top to right-bottom
        printBoard(board)
        print()
        print('Game Over\n')
        print("***** " + turn + ' won, Congratulations.*****')
        return True
    elif (board['3'] == board['5'] == board['7']) and (board['3'] != ' '):  # Diagonal right-top to left-bottom
        printBoard(board)
        print()
        print('Game Over\n')
        print("***** " + turn + ' won, Congratulations.*****')
        return True
    else:
        return False

def restart_game():
    print('wanna play again?' + ' y/n')
    start = input()
    if start == 'y':
        game()
    else:
        print("Thanks for playing! See you later.")


def game():
    mainBoard = {'1': '1', '2': '2', '3': '3',
                 '4': '4', '5': '5', '6': '6',
                 '7': '7', '8': '8', '9': '9'}
    printBoard(mainBoard)
    for key in mainBoard.keys():  # cleaning the board
        mainBoard[key] = ' '

    print('choose your symbol. X or O')
    turn = input()
    move_counter = 0

    for i in range(10):  # Game goes to atmost 9 moves

        print()
        printBoard(mainBoard)
        print("\nIt's " + turn + "'s turn. Please choose the grid number to make your move?\n")

        move = input()

        while (mainBoard[move] != ' '):
            print("\nThis place is already filled. Choose a valid place\n")  # Keep taking input until the move is valid
            move = input()

        mainBoard[move] = turn
        move_counter += 1

        if move_counter > 4:
            if (checkWinner(mainBoard, turn)):
                restart_game()
                break

        if move_counter == 9:
            print()
            print('Game Over')
            print("\nIt's a Tie\n")
            restart_game()

        if turn == 'X':  # Change turns
            turn = 'O'
        else:
            turn = 'X'

game()
