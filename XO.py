import random
import copy

X = "X"
O = "O"
EMPTY_MARK = " "


def create_empty_filed():
    return [
        [EMPTY_MARK for _ in range(3)] for _ in range(3)
    ]


def handle_move(field, move, sign):
    x, y = move
    field[x][y] = sign
    return field


def get_user_move(field):
    while True:
        s = input("Введите координаты [1-3] [1-3]")
        if len(s) != 3:
            print("Введите два числа через пробел")
            continue
        s = s.split()
        if len(s) != 2:
            print("Введите два числа через пробел")
            continue
        try:
            x, y = int(s[0]), int(s[1])
        except Exception as e:
            print("Введите два числа через пробел")
            continue
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Введите координаты от 1 до 3")
            continue

        if field[x - 1][y - 1] != EMPTY_MARK:
            print("Введите координаты свободной ячейки")
            continue
        return [x - 1, y - 1]


def check_win(field, sign):
    if field[0][0] == sign and field[1][1] == sign and field[2][2] == sign:
        return True
    if field[2][0] == sign and field[1][1] == sign and field[0][2] == sign:
        return True
    for i in range(3):
        if field[i][0] == sign and field[i][1] == sign and field[i][2] == sign:
            return True
    for i in range(3):
        if field[0][i] == sign and field[1][i] == sign and field[2][i] == sign:
            return True
    return False


def get_ai_move(field):
    for i in range(3):
        for j in range(3):
            if field[i][j] == EMPTY_MARK:
                field = handle_move(field, [i, j], O)
                if check_win(field, O):
                    field[i][j] = EMPTY_MARK
                    return [i, j]
                else:
                    field[i][j] = EMPTY_MARK

    for i in range(3):
        for j in range(3):
            if field[i][j] == EMPTY_MARK:
                field = handle_move(field, [i, j], X)
                if check_win(field, X):
                    field[i][j] = EMPTY_MARK
                    return [i, j]
                else:
                    field[i][j] = EMPTY_MARK

    i, j = random.randint(0,2), random.randint(0,2)
    while field[i][j] != EMPTY_MARK:
        i, j = random.randint(0, 2), random.randint(0, 2)
    return [i, j]


def print_field(field):
    print("_" * 12)
    for i in range(3):
        print("|   |   |   |")
        line = "|"
        for j in range(3):
            line = line + " " + field[i][j] + " |"
        print(line)
        print("|___|___|___|")


def check_draw(filed):
    for i in range(3):
        for j in range(3):
            if filed[i][j] == EMPTY_MARK:
                return False
    return True


def main():
    field = create_empty_filed()
    while True:
        print_field(field)
        move = get_user_move(field)
        field = handle_move(field, move, X)
        print_field(field)
        if check_win(field, X):
            res = X
            break
        if check_draw(field):
            res = "D"
            break
        move = get_ai_move(field)
        field = handle_move(field, move, O)
        print_field(field)
        if check_win(field, O):
            res = O
            break
        if check_draw(field):
            res = "D"
            break
    if res == "D":
        print("Ничья")
    else:
        print("Победа {}".format(res))


if __name__ == "__main__":
    main()
