board = ["_" for x in range(9)] # create spaces in the board to input the X and O


score = [0, 0]
def print_board():  # create a function that prints the board
    row =   " ___ ___ ___ "
    row1 = "|_{}_|_{}_|_{}_|".format(board[0],board[1],board[2])
    row2 = "|_{}_|_{}_|_{}_|".format(board[3],board[4],board[5])
    row3 = "|_{}_|_{}_|_{}_|".format(board[6],board[7],board[8]) # format substitutes value into {}

    print()
    print(row) # print board
    print(row1)
    print(row2)
    print(row3)
    print()

def place_value(value):  #function to place the X and O on the board
    if value == "X":
        player = 1
    elif value == "O":
        player = 2

    print("Your turn player {}".format(player)) # get input from user
    location = int(input("Enter a value corresponding to your chosen location (0 - 9): ").strip())
    if board[location - 1] == "_": # check is position has benn taken
        board[location - 1] = value
    else:
        print("\nSorry! You can't play there.")
    
def winner(value): #check if there is a winner
    if  (board[0] == value and board[1] == value and board[2] == value) or \
        (board[3] == value and board[4] == value and board[5] == value) or \
        (board[6] == value and board[7] == value and board[8] == value) or \
        (board[0] == value and board[3] == value and board[6] == value) or \
        (board[1] == value and board[4] == value and board[7] == value) or \
        (board[2] == value and board[5] == value and board[8] == value) or \
        (board[0] == value and board[4] == value and board[8] == value) or \
        (board[2] == value and board[4] == value and board[6] == value):
        return 1
    else: 
        return 0

def draw(): # check if it is a draw
    if "_" not in board:
        return 1
    else:
        return 0

def score_board(): # create a score board
    print("(player 1) {} - {} (player 2)".format(score[0],score[1]))

def demo_board(): # create a demo board so the user knows the positions on the board
    demo_board = [(x+1) for x in range(9)]
    demo_row =   " ___ ___ ___ "
    demo_row1 = "|_{}_|_{}_|_{}_|".format(demo_board[0],demo_board[1],demo_board[2])
    demo_row2 = "|_{}_|_{}_|_{}_|".format(demo_board[3],demo_board[4],demo_board[5])
    demo_row3 = "|_{}_|_{}_|_{}_|".format(demo_board[6],demo_board[7],demo_board[8])

    print()
    print(demo_row)
    print(demo_row1)
    print(demo_row2)
    print(demo_row3)
    print()

def play_game(): # start the game
    while (1): # run until a function returns false or breaks
        print_board()

        place_value("X") # player 1's turn
        print_board()
        if winner("X"):
            player = 1
            print(("Player {} wins!🥳".format(player)))
            score[0] += 1
            score_board()
            if score[0] < 2:
                for x in range(9):
                    board[x] = "_"
                play_game()
            else:
                print("Player {} is the ultimate winner. Hurray!!!🥳🥳🥳".format(player))
                break
            break
            
        elif draw():
            print("It's a draw! No one wins!")
            if score[0] < 2:
                for x in range(9):
                    board[x] = "_"
                play_game()
            else:
                break
            break
        
        place_value("O") #player 2's turn
        print_board()
        if winner("O"):
            player = 2
            print(("Player {} wins!🥳".format(player)))
            score[1] += 1
            score_board()
            if score[1] < 2:
                for x in range(9):
                    board[x] = "_"
                play_game()
            else:
                print("Player {} is the ultimate winner! Hurray!!!🥳🥳🥳".format(player))
                break
            break
        elif draw():
            print("It's a draw! No one wins!")
            if score[1] < 2:
                for x in range(9):
                    board[x] = "_"
                play_game()
            else:
                break
            break

def main(): # start the program
    print("Are you ready to play a real game of tic tac toe?")
    ready = int(input("Input 1 for yes and 0 for no: "))
    if ready == 1:
        print("This is a demo of all the positions on the board")
        print()
        demo_board()
        print("Get set, Begin!")
        print()
        play_game()
    else:
        print("You've missed out on a real game!!!")

if __name__ == "__main__":
    main()