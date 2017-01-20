'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board
    
def square_num(num):
    row = (num - 1) // 3
    column = (num % 3) - 1
    list = [row, column]
    return list 

def put_in_board(board, mark, square_number):
    list = square_num(square_number)
    board[list[0]][list[1]] = mark
    
def one_vs_one():
    i = 1
    while i < 11:
        move = int(input("Enter your move: ")
        if i % 2 != 0:
            put_in_board(board, "X", move)
            print_board_and_legend(board)
        else:
            put_in_board(board, "O", move)
            print_board_and_legend(board)
        i += 1
    

    
    
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    put_in_board(board, "X", 5)    
    print_board_and_legend(board)
    
    board = make_empty_board()
    print_board_and_legend(board) 
    #one_vs_one()
    