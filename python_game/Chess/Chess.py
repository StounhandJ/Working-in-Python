area = [
	{
			"chessPiece":"Pawn",
			"coordinates":[2, 3],
			"player": 0
			},
]

class Area:
	"""
	Игровое поле
	"""

	def __init__(self,area:list):
		self.area = area

	def deletePiece(self, x,y):
		r""" Удалить фигуру по заддоному положению на поле

		:param x: Положение по x
		:param y: Положение по y
		"""
		for mas in range(0,len(self.area)):
			if self.area[mas]["coordinates"][0]==x and self.area[mas]["coordinates"][1]==y:
				del self.area[mas]
				break

	def movePiece(self,oldX,oldY,newX,newY):
		r"""Перемещение фигуры на поле (Никаких проверок на позицию не проводиться)

		:param oldX: Положение фигуры по X
		:param oldY: Положение фигуры по Y
		:param newX: Новое положение фигуры по X
		:param newY: Новое положение фигуры по Y
		"""
		for mas in range(0,len(self.area)):
			if self.area[mas]["coordinates"][0] == oldX and self.area[mas]["coordinates"][1] == oldY:
				self.area[mas]["coordinates"][0]=newX
				self.area[mas]["coordinates"][1]=newY


class ChessPiece:
	"""Фигура"""

	def __init__(self, x, y,player, area:list):
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
		if x>7 or x<0 or y>7 or y<0:
			return False
		self.newX = x
		self.newY = y
		if self.check() and not self.checkFriendlyFigure(x,y):
			if self.checkEnemyFigure(x,y):
				self.Area.deletePiece(x,y) #Удаление вражеской фигуры на новой позиции
			self.Area.movePiece(self.oldX,self.oldY,x,y) #Перемещение фигуры на новое место
			return True
		return False

	def checkRoad(self):
		""" Проверка на фигуры на пути

		:return: Можно ли ходить
		:rtype: bool
		"""
		for mas in self.Area.area:
			x = mas["coordinates"][0]
			y = mas["coordinates"][1]

			dx1 = self.newX - self.oldX
			dy1 = self.newY - self.oldY;

			dx = x - self.oldX
			dy = y - self.oldY

			S = dx1 * dy - dx * dy1

			PX = (self.newX - self.oldX)
			PY = (self.newY - self.oldY)
			if PX==0 or PY==0:
				maxX = self.newX if self.newX>self.oldX else self.oldX
				minX = self.newX if self.newX < self.oldX else self.oldX
				maxY = self.newY if self.newY > self.oldY else self.oldY
				minY = self.newY if self.newY < self.oldY else self.oldY
				if (maxX!=minX and minX<x<maxX and y==self.newY) or (maxY!=minY and minY<y<maxY and x==self.newX):
					return False
			else:
				if (x - self.oldX) / PX == (y - self.oldY) / PY:
					if self.checkEnemyFigure(self.newX,self.newY) and self.checkFriendlyFigure(self.newX,self.newY):
						if self.oldX != x and self.oldY != y:
							return False
		return True

	def checkEnemyFigure(self,x,y):
		""" Проверка вражеской фигуры на данной позиции

		:param x: Положение проверки по X
		:param y: Положение проверки по Y
		:return: Есть ли фигура в данном месте
		:rtype: bool
		"""
		for mas in self.Area.area:
			if mas["coordinates"][0]==x and mas["coordinates"][1]==y and self.player!=mas["player"]:
				return True
		return False

	def checkFriendlyFigure(self,x,y):
		"""Проверка дружеской фигуры на данной позиции

		:param x: Положение проверки по X
		:param y: Положение проверки по Y
		:return: Есть ли фигура в данном месте
		:rtype: bool
		"""
		for mas in self.Area.area:
			if mas["coordinates"][0]==x and mas["coordinates"][1]==y and self.player==mas["player"]:
				return True
		return False

	# interface
	def check(self):
		""" Проверка хода для фигурыы

		:return: Возможен ли ход
		:rtype: bool
		"""
		pass


class Pawn(ChessPiece):
	"""
	Пешка
	"""

	def check(self):
		vrem = self.oldX - self.newX
		vrem2 = self.oldY - self.newY
		posX = vrem * -1 if (vrem < 0) else vrem
		posY = vrem2 * -1 if (vrem2 < 0) else vrem2
		print((self.player==1 and vrem2>0),(self.player==1 and vrem2<0))
		print((self.player==1 and vrem2>0) or (self.player==1 and vrem2<0))
		if (((posY==1 and posX==0) or (posY==2 and (self.oldY==6 or self.oldY==1))) and ((self.player==1 and vrem2<0) or (self.player==2 and vrem2>0))) or (posY==1 and posX==1 and self.checkEnemyFigure(self.newX,self.newY)):
			return self.checkRoad()
		return False

class Rook(ChessPiece):
	"""
	Ладья
	"""

	def check(self):
		vrem = self.oldX - self.newX
		vrem2 = self.oldY - self.newY
		posX = vrem * -1 if (vrem < 0) else vrem
		posY = vrem2 * -1 if (vrem2 < 0) else vrem2
		if (posY==0 and posX>0) or (posX==0 and posY>0):
			return self.checkRoad()
		return False

class Horse(ChessPiece):
	"""
	Конь
	"""

	def check(self):
		vrem = self.oldX - self.newX
		vrem2 = self.oldY - self.newY
		posX = vrem * -1 if (vrem < 0) else vrem
		posY = vrem2 * -1 if (vrem2 < 0) else vrem2
		if (posY==2 and posX==1) or (posX==2 and posY==1):
			return True
		return False

class Bishop(ChessPiece):
	"""
	Слон
	"""

	def check(self):
		vrem = self.oldX - self.newX
		vrem2 = self.oldY - self.newY
		posX = vrem * -1 if (vrem < 0) else vrem
		posY = vrem2 * -1 if (vrem2 < 0) else vrem2
		if posY == posX:
			return self.checkRoad()
		return False

class Queen(ChessPiece):
	"""
	Королева
	"""

	def check(self):
		vrem = self.oldX - self.newX
		vrem2 = self.oldY - self.newY
		posX = vrem * -1 if (vrem < 0) else vrem
		posY = vrem2 * -1 if (vrem2 < 0) else vrem2
		if (posY == posX) or ((posY==0 and posX>0) or (posX==0 and posY>0)):
			return self.checkRoad()
		return False

class King(ChessPiece):
	"""
	Король
	"""

	def check(self):
		vrem = self.oldX - self.newX
		vrem2 = self.oldY - self.newY
		posX = vrem * -1 if (vrem < 0) else vrem
		posY = vrem2 * -1 if (vrem2 < 0) else vrem2
		if posY<=1 and posX<=1:
			return self.checkRoad()
		return False