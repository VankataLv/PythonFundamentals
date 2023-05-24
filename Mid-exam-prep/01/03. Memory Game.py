board = input().split(" ")
moves = 0
command = input()
while command != "end":
    first_index, second_index = command.split(" ")
    first_index = int(first_index)
    second_index = int(second_index)
    if first_index == second_index or first_index not in range(0, len(board)) or second_index not in range(0, len(board)):
        middle_board = len(board) // 2
        moves += 1
        board.insert(middle_board, f"-{moves}a")
        board.insert(middle_board, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if board[first_index] == board[second_index]:
            print(f'Congrats! You have found matching elements - {board[first_index]}!')
            board.pop(min(first_index, second_index))
            board.pop(max(first_index, second_index) - 1)
            moves += 1
        else:
            print("Try again!")
            moves += 1
    if len(board) == 0:
        print(f"You have won in {moves} turns!")
        quit()
    command = input()
print("Sorry you lose :(")
print(" ".join(board))

