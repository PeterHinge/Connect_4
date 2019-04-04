import pygame
import pandas as pd


GREEN = "green"
RED = "red"


def setup():  # Sets up board.
    board = [[None for i in range(6)] for list in range(7)]
    return board


def turn(board, player, move):  # Plays through turn
    for index in range(len(board[move])):

        if board[move][index] is None:

            if player == GREEN:
                board[move][index] = GREEN
            elif player == RED:
                board[move][index] = RED

            if check_for_win(board, player, move, index):
                return player

            return board


def check_for_win(board, player, x, y):  # Checks if the current move results in win.
    possible_options = get_adjacent_cells(x, y)
    for option in possible_options:

        if inside_board(option[0], option[1]) and board[option[0]][option[1]] == player:
            x_direction, y_direction = option[0]-x, option[1]-y

            if inside_board(option[0] + x_direction, option[1] + y_direction) and \
                    board[option[0] + x_direction][option[1] + y_direction] == player:
                if inside_board(option[0] + x_direction*2, option[1] + y_direction*2) and \
                        board[option[0] + x_direction*2][option[1] + y_direction*2] == player:
                    return True
                elif inside_board(x + x_direction*-1, y + y_direction*-1) and \
                        board[x + x_direction*-1][y + y_direction*-1] == player:
                    return True

            elif inside_board(x + x_direction * -1, y + y_direction * -1) and \
                    board[x + x_direction * -1][y + y_direction * -1] == player:
                if inside_board(x + x_direction*-2, y + y_direction*-2) and \
                        board[x + x_direction*-2][y + y_direction*-2] == player:
                    return True
    return False


def get_adjacent_cells(x, y):  # Checks and return adjacent cells.
    adjacent_cells = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
    for cell in adjacent_cells:
        cell[0] += x
        cell[1] += y
    return adjacent_cells


def inside_board(x, y):
    return 0 <= x <= 6 and 0 <= y <= 7


b = setup()

player_turn = GREEN

print(pd.DataFrame(b))

while True:
    play = int(input("Where to play? "))
    if b[play][5] is None:
        b = turn(b, player_turn, play)
        if b == player_turn:
            print("{} wins!".format(player_turn))
            break
        print("Moved made.")
        if player_turn == GREEN:
            player_turn = RED
        elif player_turn == RED:
            player_turn = GREEN
    else:
        print("You can't play there. Try again somewhere else.")
    print(pd.DataFrame(b))
