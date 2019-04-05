import random
import pygame
import pandas as pd


GREEN = "green"
RED = "red"


def setup():  # Sets up board.
    board = [[None for i in range(7)] for list in range(7)]
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

        try:

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
        except:
            return False
    return False


def get_adjacent_cells(x, y):  # Checks and return adjacent cells.
    adjacent_cells = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]
    for cell in adjacent_cells:
        cell[0] += x
        cell[1] += y
    return adjacent_cells


def inside_board(x, y):
    return 0 <= x <= 6 and 0 <= y <= 7


class AI:
    def __init__(self, color=RED, strength=1):
        self.color = color
        self.strength = strength
        print("ai on")

    def evaluate(self, board):
        ai_board = board
        best_move = None
        candidate_moves = []
        for move in range(len(ai_board)):

            if ai_board[move][5] is None:
                for index in range(len(ai_board[move])):

                    if ai_board[move][index] is None:
                        ai_board[move][index] = self.color
                        if check_for_win(ai_board, self.color, move, index):
                            ai_board[move][index] = None
                            return move
                        else:
                            candidate_moves.append(move)
                            ai_board[move][index] = None

        for move in candidate_moves:
            best_move = random.randint(0, move)

        return best_move

    def play(self, board):
        move_to_play = self.evaluate(board)
        board = turn(board, self.color, move_to_play)
        return board


b = setup()

player_turn = GREEN

AI_on = False

turn_on_ai = input("AI on? ")
if turn_on_ai == "y":
    AI_on = True

print(pd.DataFrame(b))

while True:
    if not AI_on:
        play = int(input("Where to play? "))

        if 0 <= play <= 5 and b[play][5] is None:
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

    elif AI_on:
        ai = AI(RED, 1)

        if player_turn == GREEN:
            play = int(input("Where to play? "))
            if b[play][5] is None:
                b = turn(b, player_turn, play)
                if b == player_turn:
                    print("{} wins!".format(player_turn))
                    break
                print("Moved made.")
                player_turn = RED
            else:
                print("You can't play there. Try again somewhere else.")

        elif player_turn == RED:
            b = ai.play(b)
            if b == player_turn:
                print("{} wins!".format(player_turn))
                break
            player_turn = GREEN

        print(pd.DataFrame(b))
