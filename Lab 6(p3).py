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

def get_free_squares(board):
    free = []
    for i in range(3):
        for p in range(3):
            if board[i][p] == " ":
                z = [i, p]
                free.append(z)
    return free
    
def make_random_move(board, mark):
    free = get_free_squares(board)
    magic_num = int(len(free) * random.random())
    board[free[magic_num][0]][free[magic_num][1]] = mark
    
    
def comp_vs_human():
    i = 1
    while i < 6:
        move = int(input("Enter your move: "))
        put_in_board(board, "X", move)
        if is_win(board, "X") == True:
            print_board_and_legend(board)
            print("you win")
            return
        make_random_move(board, "O")
        print_board_and_legend(board)
        if is_win(board, "O") == True:
            print("you lose")
            return 
        i += 1
    
def is_row_all_marks(board, row_i, mark):
    count = 0
    for i in range(3):
        if board[row_i][i] == mark:
            count += 1
    if count == 3:
        return True
    return False 

def is_col_all_marks(board, col_i, mark):
    count = 0 
    for i in range(3):
        if board[i][col_i] == mark:
            count += 1
    if count == 3:
        return True
    return False
    
def is_win(board, mark):
    for i in range(3):
        if is_row_all_marks(board, i, mark) == True:
            return True
        if is_col_all_marks(board, i, mark) == True:
            return True 
    if board[1][1] == mark:
        if board[0][0] == mark and board[2][2] == mark:
            return True
        if board[0][2] == mark and board[2][0] == mark:
            return True
    return False
  
def optimal_move(board, mark):
    free = get_free_squares(board)
    for i in range(len(free)):
        board[free[i][0]][free[i][1]] = mark
        if is_win(board, mark) == True:
            return i 
        board[free[i][0]][free[i][1]] = " "
    # make_random_move(board, mark)

def optimal_game():
    #first move
    move1 = int(input("Enter your move: "))
    if move1 == 5:
        put_in_board(board, "X", 1)
    if move1 != 5:
        put_in_board(board, "X", 5)
         move = int(input("Enter your move: ")) 
    
    
    i = 1
    while i < 6:
        move = int(input("Enter your move: "))
        put_in_board(board, "X", move)
        if is_win(board, "X") == True:
            print_board_and_legend(board)
            print("you win")
            return
        
            
        make_random_move(board, "O")
        print_board_and_legend(board)
        if is_win(board, "O") == True:
            print("you lose")
            return 
        i += 1
    

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    comp_vs_human()