def print_horiz_line():
    print(" --- " * board_size)

def print_vert_line():
    print("|   " * (board_size + 1))

if __name__ == "__main__":
    board_size = int(raw_input("What is the size of game board? "))
    for index in range(board_size):
        print_horiz_line()
        print_vert_line()

