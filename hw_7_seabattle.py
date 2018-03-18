import functools

FIELD_SIZE = 10
SHIP4 = 1
SHIP3 = 2
SHIP2 = 3
SHIP1 = 4

EMPTY_MARK = "~"
SHIP_MARK = "="
HIT_MARK = "X"
MISS_MARK = "o"

AUTO_EMPTY_SHOT = True


class ShipPositionException(Exception):
    pass


class ShotPositionException(Exception):
    pass


class Player:
    def __init__(self, name):
        self.name = name

    def get_shot(self):
        while True:
            try:
                xy = input("{}, введите координаты выстрела <X Y> ".format(self.name))
                x, y = list(map(int, xy.split()))
            except Exception:
                print("Введите корректные координаты")
                continue
            shot = Shot(x, y)
            break
        return shot

    def get_ship_position(self, deck):
        while True:
            try:
                xy = input("{}, введите позицию {}-палубного корабля <X1, Y1, X2, Y2> ".format(self.name, deck))
                begin_x, begin_y, end_x, end_y = list(map(int, xy.split()))
                if (begin_x != end_x) and (begin_y != end_y) and deck != 1:
                    raise ShipPositionException("Корабль может располагаться только вертикально или горизонтально")
                if abs((begin_x - end_x) + (begin_y - end_y)) + 1 != deck:
                    raise ShipPositionException("Координаты не совпадают с размером корабля")
            except ShipPositionException as e:
                print(e)
                continue
            except Exception:
                 print("Введите корректные координаты")
                 continue
            break

        if begin_x > end_x:
            begin_x, end_x = end_x, begin_x
        if begin_y > end_y:
            begin_y, end_y = end_y, begin_y
        return begin_x, begin_y, end_x, end_y

class Field:
    def __init__(self, size, player, *args):
        self.size = size
        self.player = player
        self.ships = []
        self.shots = []

        self.str_field = [
            [EMPTY_MARK for _ in range(self.size)]
            for _ in range(self.size)
        ]

        for deck, count in enumerate(args, 1):
            for i in range(1, count + 1):
                ship = Ship(deck)
                self.ships.append(ship)

    def input_ship_position(self):
        for ship in self.ships:
            deck = ship.deck
            self.print_field()
            while True:
                try:
                    begin_x, begin_y, end_x, end_y = self.player.get_ship_position(deck)
                    if not (1 <= begin_x <= self.size):
                        raise ShipPositionException("Координаты выходят за пределы поля")
                    if not (1 <= end_x <= self.size):
                        raise ShipPositionException("Координаты выходят за пределы поля")
                    if not (1 <= begin_y <= self.size):
                        raise ShipPositionException("Координаты выходят за пределы поля")
                    if not (1 <= end_y <= self.size):
                        raise ShipPositionException("Координаты выходят за пределы поля")

                    for x in range(begin_x, end_x + 1):
                        for y in range(begin_y, end_y + 1):
                            if not self.check_hit(x, y) is False:
                                raise ShipPositionException("Координата {} {} занята".format(x, y))

                            if not self.check_hit(x, y - 1) is False:
                                raise ShipPositionException("Корабли не должны соприкасаться")
                            if not self.check_hit(x, y + 1) is False:
                                raise ShipPositionException("Корабли не должны соприкасаться")
                            if not self.check_hit(x - 1, y) is False:
                                raise ShipPositionException("Корабли не должны соприкасаться")
                            if not self.check_hit(x - 1, y - 1) is False:
                                raise ShipPositionException("Корабли не должны соприкасаться")
                            if not self.check_hit(x - 1, y + 1) is False:
                                raise ShipPositionException("Корабли не должны соприкасаться")
                            if not self.check_hit(x + 1, y) is False:
                                raise ShipPositionException("Корабли не должны соприкасаться")
                            if not self.check_hit(x + 1, y - 1) is False:
                                raise ShipPositionException("Корабли не должны соприкасаться")
                            if not self.check_hit(x + 1, y + 1) is False:
                                raise ShipPositionException("Корабли не должны соприкасаться")

                except ShipPositionException as e:
                    print(e)
                    continue
                except Exception as e:
                    print("Введите корректные координаты")
                    continue

                ship.set_position(begin_x, begin_y, end_x, end_y)
                self.add_ship_to_print(ship)
                break

        for ship in self.ships:
            self.clear_ship_to_print(ship)

    def check_hit(self, x, y):
        for ship in self.ships:
            begin_x, begin_y, end_x, end_y = ship.begin_x, ship.begin_y, ship.end_x, ship.end_y
            if (begin_x <= x <= end_x) and (begin_y <= y <= end_y):
                return ship
        return False

    def add_ship_to_print(self, ship):
        for x in range(ship.begin_x, ship.end_x + 1):
            for y in range(ship.begin_y, ship.end_y + 1):
                self.str_field[x - 1][y - 1] = SHIP_MARK

    def clear_ship_to_print(self, ship):
        for x in range(ship.begin_x, ship.end_x + 1):
            for y in range(ship.begin_y, ship.end_y + 1):
                self.str_field[x - 1][y - 1] = EMPTY_MARK

    def add_hit_to_print(self, shot):
        self.str_field[shot.x - 1][shot.y - 1] = HIT_MARK if shot.hit else MISS_MARK

    def print_field(self):
        line = "   " + functools.reduce(lambda x, y: x + y[-1], list(map(str, range(1, 11))))
        print(line)
        print("  " + "*" * (self.size + 2))
        for i in range(self.size):
            line = str(i+1)[-1] + " *" + functools.reduce(lambda x, y: x + y, self.str_field[i]) + "*"
            print(line)
        print("  " + "*" * (self.size + 2))

    def check_win(self):
        for ship in self.ships:
            if ship.life > 0:
                return False
        return True

    def add_shot(self, shot):
        self.shots.append(shot)
        x = shot.x
        y = shot.y
        ship = self.check_hit(x, y)
        if ship is False:
            shot.set_hit(False)
        else:
            shot.set_hit(True)
            ship.hitting()
            if ship.life == 0 and AUTO_EMPTY_SHOT:
                for x in range(ship.begin_x, ship.end_x + 1):
                    for y in range(ship.begin_y, ship.end_y + 1):
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                if dx != 0 and dy !=0:
                                    empty_x = x + dx
                                    empty_y = y + dy
                                    if (ship.begin_x <= empty_x <= ship.end_x) and \
                                            (ship.begin_y <= empty_y <= ship.end_y):
                                        continue
                                    if empty_x < 1 or empty_x > self.size or empty_y < 1 or empty_y > self.size:
                                        continue
                                    auto_empty_shot = Shot(empty_x, empty_y)
                                    self.add_shot(auto_empty_shot)

        self.add_hit_to_print(shot)
        return shot.hit


class Ship:
    def __init__(self, deck):
        self.deck = deck
        self.life = deck

        self.begin_x = -1
        self.begin_y = -1
        self.end_x = -1
        self.end_y = -1

    def set_position(self, begin_x, begin_y, end_x, end_y):
        self.begin_x = begin_x
        self.begin_y = begin_y
        self.end_x = end_x
        self.end_y = end_y

    def hitting(self):
        self.life -= 1


class Shot():
    def __init__(self, x, y):
        self.x, self.y = x, y

    def set_hit(self, hit):
        self.hit = hit
        # field.check_hit(x, y)

    def __contains__(self, item):
        return (self.x == item.x) and (self.y == item.y)


class Game():
    def __init__(self):
        player1 = Player("Игрок1")
        player2 = Player("Игрок2")

        self.players = [player1, player2]

        # field1 = Field(FIELD_SIZE, player1, SHIP1, SHIP2, SHIP3, SHIP4)
        # field2 = Field(FIELD_SIZE, player2, SHIP1, SHIP2, SHIP3, SHIP4)

        field1 = Field(FIELD_SIZE, player1, 0, 2)
        field2 = Field(FIELD_SIZE, player2, 0, 2)

        self.fields = [field1, field2]

        self.turn = 0

    def input_ship_position(self):
        for field in self.fields:
            field.input_ship_position()
        self.fields.reverse()

    def change_turn(self):
        self.turn = 1 if self.turn == 0 else 0

    def check_win(self):
        field = self.fields[self.turn]
        return field.check_win()

    def print_field(self):
        self.fields[self.turn].print_field()

    def shooting(self):
        field = self.fields[self.turn]
        player = self.players[self.turn]
        while True:
            try:
                shot = player.get_shot()
                x, y = shot.x, shot.y
                if not (1 <= x <= field.size):
                    raise ShotPositionException("Координаты выходят за пределы поля")
                if not(1 <= y <= field.size):
                    raise ShotPositionException("Координаты выходят за пределы поля")

                if shot in field.shots:
                    raise ShotPositionException("Вы уже стреляли по этим координатам")

            except ShotPositionException as e:
                print(e)
                continue

            break
        if not field.add_shot(shot):
            self.change_turn()

    def play(self):
        self.input_ship_position()
        while not self.check_win():
            self.print_field()
            self.shooting()


game = Game()
game.play()
