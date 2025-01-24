#Final PETA -- Game Console


import random

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def tis_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def sudoku(board):
    print_board(board)
    while True:
        command = input("Type 'exit' to quit or enter your move (row col num): ")
        if command.lower() == 'exit':
            print("Exiting Sudoku...")
            break
        try:
            row, col, num = map(int, command.split())
            if not (0 <= row < 9) or not (0 <= col < 9) or not (1 <= num <= 9):
                print("Invalid input! Please enter numbers within the specified range (row: 0-8, col: 0-8, num: 1-9).")
                continue
            
            if tis_valid(board, row, col, num):
                board[row][col] = num
                print_board(board)
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter valid input (row, column, number) or 'exit'.")

def initialize_board(size, mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mine_positions = set()
    while len(mine_positions) < mines:
        mine_positions.add((random.randint(0, size - 1), random.randint(0, size - 1)))
    for pos in mine_positions:
        board[pos[0]][pos[1]] = '*'
    return board, mine_positions

def minesweeper_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('.', end=' ')
        print()

def minesweeper(size=5, mines=3):
    board, mine_positions = initialize_board(size, mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    
    while True:
        minesweeper_board(board, revealed)
        command = input("Type 'exit' to quit or enter your move (row, column): ")
        if command.lower() == 'exit':
            print("Exiting Minesweeper...")
            break
        try:
            row, col = map(int, command.split())
            if not (0 <= row < size) or not (0 <= col < size):
                print("Invalid input! Please enter numbers within the specified range (row: 0-{}, col: 0-{}).".format(size-1, size-1))
                continue
            
            if (row, col) in mine_positions:
                print("Game Over! You hit a mine!")
                break
            
            revealed[row][col] = True
        except ValueError:
            print("Please enter valid input (row, column) or 'exit'.")

def main_menu():
    while True:
        print("Welcome to the Game Menu!")
        print("1. Play Sudoku")
        print("2. Play Minesweeper")
        print("3. Exit")
        
        choice = input("Choose a game (1-3): ")
        
        if choice == '1':
            print ("Wecome to Sudoku, To play please type the following format. eg: If you want to place the number 5 in the cell at row 0, column 1, you would enter: 0 1 5")
            sudoku_board = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
            sudoku(sudoku_board)
        
        elif choice == '2':
            print ("Welcome to MineSweeper, To play this game please type the following format. eg: If you want to reveal the cell at row 1, column 2, you would enter: 1 2")
            minesweeper(size=5, mines=3)
        
        elif choice == '3':
            print("Thank you for playing!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main_menu()
