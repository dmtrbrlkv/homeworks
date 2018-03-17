# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = '[]'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

# WIN_FILED = list(map(str, range(1, 16)))
WIN_FILED = list(range(1, 16))
WIN_FILED.append(EMPTY_MARK)

SHUFFLE_N = 100
COUNT_MOVES = 0


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """

    def random_move(lastmove):
        move = random.sample(MOVES.keys(), 1)[0]
        if (move == "w" and lastmove == "s") or \
                (move == "s" and lastmove == "w") or \
                (move == "a" and lastmove == "d") or \
                (move == "d" and lastmove == "a"):
            return random_move(lastmove)
        else:
            return move

    field = WIN_FILED.copy()
    # random.shuffle(field)

    i = 1
    move = "w"
    while i <= SHUFFLE_N:
        try:
            move = random_move(move)
            perform_move(field, move)
            # print_field(field)
            # print("")
            i = i + 1
        except IndexError:
            pass

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(4):
        print("\t".join(list(map(str, field[i * 4 + 0:i * 4 + 4]))))


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """

    return field == WIN_FILED


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """

    empty_index = field.index(EMPTY_MARK)
    move_index = empty_index + MOVES[key]
    if move_index < 0 or move_index > len(field):
        raise IndexError("Недопустимый ход")
    else:
        empty_index_x = (empty_index) // 4 + 1
        empty_index_y = (empty_index + 1) % 4 + 1

        move_index_x = (move_index) // 4 + 1
        move_index_y = (move_index + 1) % 4 + 1

        if (empty_index_x != move_index_x) and (empty_index_y != move_index_y):
            raise IndexError("Недопустимый ход")

    field[empty_index], field[move_index] = field[move_index], field[empty_index]
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """

    move = ""
    while move not in MOVES:
        move = input("Ход: ")
    return move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """
    try:
        field = shuffle_field()
        user_moves = 0
        while not is_game_finished(field):
            print_field(field)
            move = handle_user_input()
            try:
                field = perform_move(field, move)
            except IndexError as e:
                print(e)
            else:
                user_moves += 1
        print("ПОБЕДА!!! Число шагов - {}".format(user_moves))
    except KeyboardInterrupt:
        print("shutting down")


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()
