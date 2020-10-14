import pygame as pg
import time
import random

pg.init()
screen = pg.display.set_mode((520, 660))
clock = pg.time.Clock()

# Цвета -------------------
red = (230, 20, 20)
green = (20, 230, 20)
green_b = (10, 120, 10)
white = (230, 230, 230)
color = [(230, 230, 230), (230, 20, 20), (20, 230, 20)]  # белый, красный, зеленый
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
    pos_y = 0
    pos_x = 5
    shape = [[1, 1], [1, 1]]

    def new_figure(self):
        pass

    def moving(self, x, y):
        self.pos_y = y
        self.pos_x = x
        return [self.pos_x, self.pos_y]


class Area:

    def __init__(self):
        self.figure = Figure()  # Объект фигуры
        self.new_x_figure = 5  # Позиция фигуры после нажатия клавиши
        self.y_shift_time = 5  # Через сколько обновлений сдивунть фигуру по y
        self.y_shift_time_now = 0  # Через сколько обновлений сдивунть фигуру по y
        self.area = []  # Поле
        pxy = 20
        self.clet = 660 / pxy  # Размер квадратиков
        for y in range(0, 20):
            self.area.append([0 for x in range(0, 10)])

    def event_click(self, ev):
        if ev == "d" or ev == "в":
            self.new_x_figure += 1
        elif ev == "a" or ev == "ф":
            self.new_x_figure -= 1

    def moving_figure(self):
        shape = self.figure.shape
        x_shape = self.figure.pos_x
        y_shape = self.figure.pos_y
        for y in range(0, len(shape)):  # Удаление прошлой позиции фигуры
            for x in range(0, len(shape[y])):
                if shape[y][x] != 0:
                    self.area[y_shape + y][x_shape + x] = 0
        self.y_shift_time_now += 1
        if self.y_shift_time_now == self.y_shift_time:
            y_shape += 1
            self.y_shift_time_now = 0
        x_shape, y_shape = self.figure.moving(self.new_x_figure, y_shape)  # Перемещение фигуры

        for y in range(0, len(shape)):  # Новое положение фигуры
            for x in range(0, len(shape[y])):
                if shape[y][x] != 0:
                    self.area[y_shape + y][x_shape + x] = shape[y][x]

    def draw(self):
        self.moving_figure()
        for x_a in range(10):
            for y_a in range(20):
                pg.draw.rect(screen, color[self.area[y_a][x_a]],
                             (self.clet * x_a, self.clet * y_a, self.clet - 5, self.clet - 5))
        Text.draw(screen, 390, 30, "Очков: 0", red)


def main():  # Основное тело программы
    start = True  # Активность игры
    area = Area()
    while start:
        screen.fill((30, 30, 30))
        area.draw()
        for event in pg.event.get():  # Проверка соытий
            if event.type == pg.QUIT:  # Событие закрытия приложения
                start = False
            elif event.type == pg.KEYDOWN:  # Нажате клавиши
                area.event_click(event.unicode)
        pg.display.flip()  # Перерисовка сцены
        clock.tick(3)  # Задержка


if __name__ == '__main__':
    main()
    pg.quit()
