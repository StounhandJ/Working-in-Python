import copy
"""
Попытаться оптимизировать и убрать лишние части если таковые имеються

"""

class Area:
    """
	Игровое поле
	"""

    def __init__(self, area: list):
        self.area = area
        self.event = ""
        self.endGame = False

    def deletePiece(self, x, y):
        r""" Удалить фигуру по заддоному положению на поле

		:param x: Положение по x
		:param y: Положение по y
		"""
        for mas in range(0, len(self.area)):
            if self.area[mas]["coordinates"][0] == x and self.area[mas]["coordinates"][1] == y:
                del self.area[mas]
                break

    def movePiece(self, oldX, oldY, newX, newY):
        r"""Перемещение фигуры на поле (Никаких проверок на позицию не проводиться)

		:param oldX: Положение фигуры по X
		:param oldY: Положение фигуры по Y
		:param newX: Новое положение фигуры по X
		:param newY: Новое положение фигуры по Y
		"""
        for mas in range(0, len(self.area)):
            if self.area[mas]["coordinates"][0] == oldX and self.area[mas]["coordinates"][1] == oldY:
                self.area[mas]["coordinates"][0] = newX
                self.area[mas]["coordinates"][1] = newY

    def checkEnd(self, player, Checkmate=False):
        """Проверяет закончилась ли игра или наступил Шах

        :param player: С стороны какого игрока проверять
        :param Checkmate: Проверять ли мат в игре
        """
        king = []
        self.event =""
        self.endGame = False
        for mas in self.area:
            if mas["chessPiece"] == "King" and mas["player"] == player:
                king = mas["coordinates"]

        if not king:
            return

        for mas in self.area:
            if mas["chessPiece"] != "King" and mas["player"] != player:
                figure = eval(f'{mas["chessPiece"]}')(mas["coordinates"][0], mas["coordinates"][1], mas["player"],
                                                      self.area)
                figure.newX = king[0]
                figure.newY = king[1]
                if figure.check(False):
                    self.event = f'Шах для {"Белых" if player == 1 else "Черных"}'
                    if Checkmate:  # Если включенеа проверка на мат
                        moves = []
                        for var in self.area:  # Проверка возможности хода для всех фигур
                            # Если возможно избежать мат, если нет то это мат
                            if var["player"] == player:
                                figureChe = eval(f'{var["chessPiece"]}')(var["coordinates"][0], var["coordinates"][1], var["player"], self.area)
                                vrem = figureChe.getPossibleMoves()
                                for g in vrem:
                                    moves.append(g)
                        if not moves:
                            self.event = f'Мат для {"Белых" if player == 1 else "Черных"}'
                            self.endGame = True

    def checkWhoGoCage(self, x, y, player):
        """ Может ли вражеская фигура сходить на данную клетку

        :param x: Позиция по X
        :param y: Позиция по Y
        :param player: Дружелюбный игрок
        :return: Есть ли
        :rtype: bool
        """
        for mas in self.area:
            if mas["player"] != player:
                figure = eval(f'{mas["chessPiece"]}')(mas["coordinates"][0], mas["coordinates"][1], mas["player"],
                                                      self.area)
                figure.newX = x
                figure.newY = y
                if figure.check() and not (x == mas["coordinates"][0] and y == mas["coordinates"][1]):
                    return True
        return False


class ChessPiece:
    """Фигура"""

    def __init__(self, x, y, player, area: list):
        """
		:param x: Положение фигуры в данный момент по X
		:param y: Положение фигуры в данный момент по Y
		:param player: Номер игрока (0/1)
		:param area: Поле игры
		"""
        self.oldX = x
        self.oldY = y
        self.newX = 0
        self.newY = 0
        self.player = player
        self.Area = Area(area)

    def move(self, x, y):
        """ Попытка на движение фигуры по полю

        :param x: Новое положение фигуры по X
        :param y: Новое положение фигуры по X
        :return: Удачно ли завешилось передвижение
        :rtype: bool
        """
        if x > 7 or x < 0 or y > 7 or y < 0:
            return False
        self.newX = x
        self.newY = y
        self.Area.checkEnd(self.player, Checkmate=True)
        if self.check() and not self.Area.endGame:
            if self.checkEnemyFigure(x, y):
                self.Area.deletePiece(x, y)  # Удаление вражеской фигуры на новой позиции
            self.Area.movePiece(self.oldX, self.oldY, x, y)  # Перемещение фигуры на новое место
            self.Area.checkEnd(2 if self.player == 1 else 1, Checkmate=True)
            return True
        return False

    def checkRoadTwo(self, startX, startY, endX, endY, x, y):
        """ Дополнительная проверка для фигуры за другой фигурой

        :param startX: Начальная X
        :param startY: Начальная Y
        :param endX: Конечная X
        :param endY: Конечная Y
        :param x: Координата точки по X
        :param y: Координата точки по Y
        :return: Истино ли это
        :rtype: bool
        """
        if x == endX and y == endY:
            return True
        PX = (endX - startX)
        PY = (endY - startY)
        dotproduct = (x - startX) * (endX - startX) + (y - startY) * (endY - startY)
        squaredlengthba = (endX - startX) * (endX - startX) + (endY - startY) * (
                endY - startY)
        if (x - startX) / PX == (y - startY) / PY and not (dotproduct < 0 or dotproduct > squaredlengthba):
            if startX != x and startY != y:
                return False
        return True

    def checkRoad(self):
        """ Проверка на фигуры на пути

		:return: Можно ли ходить
		:rtype: bool
		"""
        for mas in self.Area.area:
            x = mas["coordinates"][0]
            y = mas["coordinates"][1]

            PX = (self.newX - self.oldX)
            PY = (self.newY - self.oldY)
            if self.checkFriendlyFigure(self.newX, self.newY):
                return False
            elif PX == 0 or PY == 0:
                maxX, minX = [self.newX, self.oldX] if self.newX > self.oldX else [self.oldX, self.newX]
                maxY, minY = [self.newY, self.oldY] if self.newY > self.oldY else [self.oldY, self.newY]
                if (maxX != minX and minX < x < maxX and y == self.newY) or (
                        maxY != minY and minY < y < maxY and x == self.newX):
                    return False
            else:
                if self.checkEnemyFigure(self.newX, self.newY):
                    for mas in self.Area.area:
                        if not self.checkRoadTwo(self.oldX, self.oldY, self.newX, self.newY, mas["coordinates"][0],
                                                 mas["coordinates"][1]):
                            return False
                dotproduct = (x - self.oldX) * (self.newX - self.oldX) + (y - self.oldY) * (self.newY - self.oldY)
                squaredlengthba = (self.newX - self.oldX) * (self.newX - self.oldX) + (self.newY - self.oldY) * (
                        self.newY - self.oldY)
                if (x - self.oldX) / PX == (y - self.oldY) / PY and not (
                        dotproduct < 0 or dotproduct > squaredlengthba) and not self.checkEnemyFigure(self.newX,
                                                                                                      self.newY):
                    if self.oldX != x and self.oldY != y:
                        return False
        return True

    def checkEnemyFigure(self, x, y):
        """ Проверка вражеской фигуры на данной позиции

		:param x: Положение проверки по X
		:param y: Положение проверки по Y
		:return: Есть ли фигура в данном месте
		:rtype: bool
		"""
        for mas in self.Area.area:
            if mas["coordinates"][0] == x and mas["coordinates"][1] == y and self.player != mas["player"]:
                return True
        return False

    def checkFriendlyFigure(self, x, y):
        """Проверка дружеской фигуры на данной позиции

		:param x: Положение проверки по X
		:param y: Положение проверки по Y
		:return: Есть ли фигура в данном месте
		:rtype: bool
		"""
        for mas in self.Area.area:
            if mas["coordinates"][0] == x and mas["coordinates"][1] == y and self.player == mas["player"]:
                return True
        return False

    def getPossibleMoves(self):
        """Возвращает все возможные ходы для фигуры по полю

        :return: Двумерный масив с координатами
        :rtype: list
        """
        mas = []
        for x in range(8):
            for y in range(8):
                self.newX = x
                self.newY = y
                if self.check():
                    mas.append([x, y])
        return mas

    def checkShahGame(self):
        """Проверка будет ли шах в следующем ходе

        :return: Бедет ли
        :rtype: bool
        """
        areaL = copy.deepcopy(self.Area)
        if self.checkEnemyFigure(self.newX, self.newY):
            areaL.deletePiece(self.newX, self.newY)  # Удаление вражеской фигуры на новой позиции
        areaL.movePiece(self.oldX, self.oldY, self.newX, self.newY)  # Перемещение фигуры на новое место
        areaL.checkEnd(self.player)
        return True if areaL.event != "" else False

    # interface
    def check(self, CheckShah=True):
        """ Проверка хода для фигурыы

        :param CheckShah: Нужно ли проверять Шах в следующем ходе(False в основном при проврки конца игры)
		:return: Возможен ли ход
		:rtype: bool
		"""
        pass


class Pawn(ChessPiece):
    """
	Пешка
	"""

    def check(self, CheckShah=True):
        vrem2 = self.oldY - self.newY
        posX = abs(self.oldX - self.newX)
        posY = vrem2 * -1 if (vrem2 < 0) else vrem2
        EnemyFigure = self.checkEnemyFigure(self.newX, self.newY)
        if (((posY == 1 and posX == 0) or (posY == 2 and posX == 0 and (self.oldY == 6 or self.oldY == 1))) and (
                (self.player == 1 and vrem2 < 0) or (self.player == 2 and vrem2 > 0)) and not EnemyFigure) or (
                posY == 1 and posX == 1 and EnemyFigure) and self.checkRoad():
            if not CheckShah:
                return True
            else:
                return not self.checkShahGame()
        return False


class Rook(ChessPiece):
    """
	Ладья
	"""

    def check(self, CheckShah=True):
        posX = abs(self.oldX - self.newX)
        posY = abs(self.oldY - self.newY)
        if (posY == 0 and posX > 0) or (posX == 0 and posY > 0) and self.checkRoad():
            if not CheckShah:
                return True
            else:
                return not self.checkShahGame()
        return False


class Horse(ChessPiece):
    """
	Конь
	"""

    def check(self, CheckShah=True):
        posX = abs(self.oldX - self.newX)
        posY = abs(self.oldY - self.newY)
        if ((posY == 2 and posX == 1) or (posX == 2 and posY == 1)) and not self.checkFriendlyFigure(self.newX,
                                                                                                     self.newY):
            if not CheckShah:
                return True
            else:
                return not self.checkShahGame()
        return False


class Bishop(ChessPiece):
    """
	Слон
	"""

    def check(self, CheckShah=True):
        posX = abs(self.oldX - self.newX)
        posY = abs(self.oldY - self.newY)
        if posY == posX and self.checkRoad():
            if not CheckShah:
                return True
            else:
                return not self.checkShahGame()
        return False


class Queen(ChessPiece):
    """
	Королева
	"""

    def check(self, CheckShah=True):
        posX = abs(self.oldX - self.newX)
        posY = abs(self.oldY - self.newY)
        if ((posY == posX) or ((posY == 0 and posX > 0) or (posX == 0 and posY > 0))) and self.checkRoad():
            if not CheckShah:
                return True
            else:
                return not self.checkShahGame()
        return False


class King(ChessPiece):
    """
	Король
	"""

    def check(self, CheckShah=True):
        posX = abs(self.oldX - self.newX)
        posY = abs(self.oldY - self.newY)
        if posY <= 1 and posX <= 1 and not self.Area.checkWhoGoCage(self.newX, self.newY, self.player):
            return self.checkRoad()
        return False

    def getPossibleMoves(self):
        """Возвращает все возможные ходы для фигуры по полю

        :return: Двумерный масив с координатами
        :rtype: list
        """
        mas = []
        for x in range(8):
            for y in range(8):
                self.newX = x
                self.newY = y
                if self.check():
                    mas.append([x, y])
        for x in range(len(mas)):
            if self.checkEnemyFigure(mas[x][0], mas[x][1]) and self.Area.checkWhoGoCage(mas[x][0], mas[x][1],
                                                                                        1 if self.player == 2 else 2):
                del mas[x]
        return mas
