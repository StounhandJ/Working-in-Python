import pygame as pg
import time
import random
from copy import deepcopy

pg.init()
screen = pg.display.set_mode((520, 660))
clock = pg.time.Clock()

# Цвета -------------------
red = (230, 20, 20)
green = (20, 230, 20)
green_b = (10, 120, 10)
white = (230, 230, 230)
color = [(230, 230, 230), (230, 20, 20), (0, 102, 0), (102, 90, 204), (0, 204, 204), (255, 128, 0), (0, 0, 255),
         (255, 0, 127), (255, 255, 153)]  # белый, красный, зеленый, фиолетовый, бюризовый, оранжевый, синий, розывый, бежевый,
# ---------------------
FONT = pg.font.Font(None, 36)
pos_x = 5
pos_y = 0
block = [[1, 1], [1, 1]]


class Text:  # Объект текста

    @staticmethod
    def draw(screen, x, y, text, color):  # 1 сцена; 2,3 позиция; 4 текст; 5 цвет
        o_text = FONT.render(text, True, color)
        text_rect = o_text.get_rect()
        text_rect.center = (x, y)
        screen.blit(o_text, text_rect)


class Figure:
    pos_y = -1
    pos_x = 3
    fig = [[[0, 1, 0], [1, 1, 1], [0, 0, 0]], [[1, 1], [1, 1]],
           [[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]], [[1, 0, 0], [1, 1, 1], [0, 0, 0]],
           [[0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 1, 1], [1, 1, 0], [0, 0, 0]], [[1, 1, 0], [0, 1, 1], [0, 0, 0]]]
    shape = fig[0]

    def __init__(self):
        self.pos_y = -1
        self.pos_x = 3
        self.shape = self.fig[random.randint(0, 6)]
        self.color = random.randint(1, 4)
        self.next_shape = self.fig[random.randint(0, len(self.fig) - 1)]
        self.next_color = random.randint(1, len(color) - 1)
        self.__paint()
        for y in range(len(self.shape)):
            for x in range(len(self.shape)):
                if self.shape[y][x] == 1:
                    self.shape[y][x] = self.color

    def new_figure(self):
        self.pos_y = -1
        self.pos_x = 3
        self.shape = deepcopy(self.next_shape)
        self.color = deepcopy(self.next_color)
        self.next_shape = self.fig[random.randint(0, len(self.fig) - 1)]
        self.next_color = random.randint(1, len(color) - 1)
        self.__paint()

    def turn_left(self, area):
        area_x = len(area[0])
        shep_turn = []
        shep_specular = self.__specularly(self.shape)
        for y in range(0, len(shep_specular[0])):
            shep_turn.append([0 for x in range(0, len(shep_specular))])
        for y in range(0, len(shep_specular)):
            for x in range(0, len(shep_specular[y])):
                shep_turn[x][y] = shep_specular[y][x]
        if (self.pos_x >= 0) and (len(shep_turn[0]) + self.pos_x <= area_x):
            if not self.__colision(shep_turn, area):
                self.shape = shep_turn

    def turn_right(self, area):
        shep_turn = []
        area_x = len(area[0])
        for y in range(0, len(self.shape[0])):
            shep_turn.append([0 for x in range(0, len(self.shape))])
        for y in range(0, len(self.shape)):
            for x in range(0, len(self.shape[y])):
                shep_turn[x][y] = self.shape[y][x]
        shep_specular = self.__specularly(shep_turn)
        if (self.pos_x >= 0) and (len(shep_specular[0]) + self.pos_x <= area_x):
            if not self.__colision(shep_specular, area):
                self.shape = shep_specular

    def __paint(self):
        for y in range(len(self.next_shape)):
            for x in range(len(self.next_shape)):
                if self.next_shape[y][x] == 1:
                    self.next_shape[y][x] = self.next_color

    def __colision(self, shape, area):
        for y in range(len(shape)):
            for x in range(len(shape)):
                if shape[y][x] != 0 and area[self.pos_y + y][self.pos_x + x] != 0:
                    return True
        return False

    def __specularly(self, shep):
        shep_specular = []
        for y in range(0, len(shep)):
            shep_specular.append([])
            for x in range(len(shep[y]) - 1, -1, -1):
                shep_specular[y].append(shep[y][x])
        return shep_specular


class Area:

    def __init__(self):
        self.figure = Figure()  # Объект фигуры
        self.area = []  # Поле
        pxy = 20
        self.clet = 660 / pxy  # Размер квадратиков
        self.area_x = 10  # Размер поя по x
        self.area_y = 20  # Размер поя по y
        for y in range(0, self.area_y):
            self.area.append([0 for x in range(0, self.area_x)])
        self.point = 0
        self.point_max = 0

    def event_click(self, ev):
        if (ev == "d" or ev == "в") and (not self.collision_x(True)):
            self.figure.pos_x += 1
        elif (ev == "a" or ev == "ф") and (not self.collision_x(False)):
            self.figure.pos_x -= 1
        elif ev == "q" or ev == "й":
            self.figure.turn_left(self.area)
        elif ev == "e" or ev == "у":
            self.figure.turn_right(self.area)
        elif ev == "s" or ev == "ы":
            self.moving_figure_y()
        elif ev == "w" or ev == "ц":
            self.figure.pos_y -= 1
        self.check()

    def check(self):
        for i in range(len(self.area)):
            if not 0 in self.area[i]:
                self.area.pop(i)
                self.area.insert(0, [0 for x in range(0, self.area_x)])
                self.point += 1
        for x in range(0, self.area_x):
            if self.area[0][x] != 0:
                self.area = []  # Поле
                for y in range(0, self.area_y):
                    self.area.append([0 for x in range(0, self.area_x)])
                self.point_max = self.point if self.point>self.point_max else self.point_max
                self.point = 0
                self.figure.new_figure()
                return

    def moving_figure_y(self):
        if self.collision_y():
            shape = self.figure.shape  # Фигруа
            for y in range(0, len(shape)):
                for x in range(0, len(shape[y])):
                    if shape[y][x] != 0:
                        self.area[self.figure.pos_y + y][self.figure.pos_x + x] = shape[y][x]
            self.figure.new_figure()
            self.check()
        else:
            self.figure.pos_y += 1

    def collision_x(self, right):
        shape = deepcopy(self.figure.shape)

        left_x = 0
        right_x = 0
        # Узнает размер пустых клеток в фигуре с права и лева
        if right:
            for x in range(len(shape) - 1, -1, -1):
                if [0 for i in range(len(shape))] == [shape[i][x] for i in range(0, len(shape))]:
                    right_x += 1
                else:
                    break
        else:
            for x in range(0, len(shape)):
                if [0 for i in range(len(shape))] == [shape[i][x] for i in range(0, len(shape))]:
                    left_x += 1
                else:
                    break

        # Проверка на стенки
        if (self.figure.pos_x + left_x == 0 and not right) or (
                self.figure.pos_x + len(shape) - right_x == self.area_x and right):
            return True

        # Колизия
        cof = 1 if right else -1
        colo = 1
        for y in range(0, len(shape)):
            for x in range(0, len(shape)):
                if shape[y][x] != 0:
                    try:
                        colo = shape[y][x]
                        shape[y][x] += self.area[self.figure.pos_y + y][self.figure.pos_x + x + cof]
                    except:
                        pass

        for y in range(0, len(shape)):
            for x in range(0, len(shape)):
                if shape[y][x] > colo and x + 1 <= len(shape):
                    if self.figure.shape[y][x] != 0: return True
        return False

    def collision_y(self):
        shape = self.figure.shape  # Фигруа
        cof = (self.area_y - self.figure.pos_y - len(shape)) * -1
        cof = cof if cof > 0 else 0
        for x in range(0, len(shape)):
            if (shape[len(shape) - 1 - cof][x] != 0) and (len(shape) + self.figure.pos_y >= self.area_y):
                return True

        for y in range(0, len(shape)):
            for x in range(0, len(shape[y])):
                if (shape[y][x] != 0) and (self.area[self.figure.pos_y + y + 1][self.figure.pos_x + x] != 0):
                    return True
        return False

    def draw(self):
        # Отрисовка поля
        for x_a in range(self.area_x):
            for y_a in range(self.area_y):
                pg.draw.rect(screen, color[self.area[y_a][x_a]],
                             (self.clet * x_a, self.clet * y_a, self.clet - 5, self.clet - 5))
        # Отрисовка объекта игры
        shape = self.figure.shape  # Фигруа
        for y in range(0, len(shape)):
            for x in range(0, len(shape[y])):
                if shape[y][x] != 0:
                    pg.draw.rect(screen, color[shape[y][x]],
                                 (self.clet * (self.figure.pos_x + x), self.clet * (self.figure.pos_y + y),
                                  self.clet - 5, self.clet - 5))
        # Отрисовка следующей фигуры
        shape = self.figure.next_shape  # Фигруа
        for y in range(0, len(shape)):
            for x in range(0, len(shape[y])):
                if shape[y][x] != 0:
                    pg.draw.rect(screen, color[shape[y][x]],
                                 (self.clet * x + 380, self.clet * y + 105, self.clet - 5, self.clet - 5))

        # Отрисовка текста
        Text.draw(screen, 390, 30, f"Очков: {self.point}", red)
        Text.draw(screen, 415, 80, "Следующая:", red)
        Text.draw(screen, 400, 200, f"Рекорд: {self.point_max}", red)


def main():  # Основное тело программы
    start = True  # Активность игры
    area = Area()
    tick = pg.time.get_ticks()
    screen.fill((30, 30, 30))
    area.draw()
    pg.display.flip()  # Перерисовка сцены
    while start:
        screen.fill((30, 30, 30))
        for event in pg.event.get():  # Проверка соытий
            if event.type == pg.QUIT:  # Событие закрытия приложения
                start = False
            elif event.type == pg.KEYDOWN:  # Нажате клавиши
                area.event_click(event.unicode)
                area.draw()
                pg.display.flip()  # Перерисовка сцены
        if pg.time.get_ticks() - tick > 50:
            area.moving_figure_y()
            area.draw()
            pg.display.flip()  # Перерисовка сцены
            tick = pg.time.get_ticks()
        tick += 1
        # clock.tick(1)  # Задержка


if __name__ == '__main__':
    main()
    pg.quit()
