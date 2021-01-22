import random
import pygame as pg

pg.init()
area = []  # Игровое поле
selected = []  # Координаты фокуса
screenXY = 720  # Размер окна в px
difficulty = 4  # Сложность игры
sizeField = 9  # Размер поля   КОНСТАНТА
sizeCell = screenXY / sizeField  # Размер одной ячейки
screen = pg.display.set_mode((screenXY, screenXY))  # Сцена
clock = pg.time.Clock()


class Text:  # Объект текста
    @staticmethod
    def draw(screen, x, y, text, color, sizeFont):
        """Отрисовка текста в определенном месте сцены.


        :param screen: Сцена
        :param x: Позиция по X
        :param y: Позиция по Y
        :param text: Текст
        :param color: Цвет текста
        :param sizeFont: Размер щрифта
        """
        FONT = pg.font.Font(None, sizeFont)
        o_text = FONT.render(text, True, color)
        text_rect = o_text.get_rect()
        text_rect.center = (x, y)
        screen.blit(o_text, text_rect)


def possiblePutNumber(x, y, n):
    for i in range(len(area)):
        if area[x][i] == n or area[i][y] == n:
            return False

    cellX = (x // 3) * 3
    cellY = (y // 3) * 3
    for i in range(len(area) // 3):
        for j in range(len(area) // 3):
            if area[cellX + i][cellY + j] == n:
                return False
    return True


def check():
    global area
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] == 0:
                for n in range(1, 10):
                    if possiblePutNumber(i, j, n):
                        area[i][j] = n
                        if check(): return True
                        area[i][j] = 0
                return False
    return True


def generationArea(x, y):
    global area, difficulty
    if x != y and x % 3 != 0 and y % 3 != 0:
        return False
    area = [[0 for j in range(y)] for i in range(x)]
    i = 0
    while 0 in area[0]:
        rand = random.randint(1, 9)
        if not (rand in area[0]):
            area[0][i] = rand
            i += 1
    check()
    deletedNumbers = []
    difficulty = difficulty if sizeField * sizeField >= difficulty * 10 else sizeField * sizeField // 10
    for cellDel in range(difficulty * 10):
        getRand = True
        while getRand:
            x = random.randint(0, sizeField - 1)
            y = random.randint(0, sizeField - 1)
            if not ([x, y] in deletedNumbers):
                deletedNumbers.append([x, y])
                getRand = False
        area[x][y] = 0
    print(1)


def draw():
    for x in range(sizeField):
        for y in range(sizeField):
            pg.draw.rect(screen, (255, 255, 255), (sizeCell * x, sizeCell * y, sizeCell - 1, sizeCell - 1))
            Text.draw(screen, sizeCell * x + sizeCell / 2, sizeCell * y + sizeCell / 2,
                      str(area[y][x]) if area[y][x] != 0 else "", (250, 16, 16), 60)

    for x in range(sizeField // 3):
        pg.draw.line(screen, (0, 0, 0), (sizeCell * (x + 1) * 3, 0), (sizeCell * (x + 1) * 3, screenXY), 5)
        pg.draw.line(screen, (0, 0, 0), (0, sizeCell * (x + 1) * 3), (screenXY, sizeCell * (x + 1) * 3), 5)

    if selected:  # Рисуем заленый квадрат фокуса для фигуры, если он есть
        pg.draw.rect(screen, (40, 250, 0), (sizeCell * selected[0], sizeCell * selected[1], sizeCell, sizeCell), 6)


def main():
    global selected, area
    start = True  # Активность игры
    tick = pg.time.get_ticks()
    screen.fill((30, 30, 30))
    draw()
    pg.display.flip()  # Перерисовка сцены
    while start:
        screen.fill((30, 30, 30))
        for event in pg.event.get():  # Проверка соытий
            if event.type == pg.QUIT:  # Событие закрытия приложения
                start = False
            elif event.type == pg.KEYDOWN:  # Нажате клавиши
                if selected and event.dict['unicode'].isdigit() and 0 <= int(event.dict['unicode']) < 10:
                    area[selected[1]][selected[0]] = int(event.dict['unicode'])

            elif event.type == pg.MOUSEBUTTONDOWN:  # Нажате клавиши

                if event.dict['button'] == 3:  # Если правая кнопка, то убрать фокус на фигуре
                    selected = []
                else:
                    x = int(event.dict['pos'][0] / sizeCell)
                    y = int(event.dict['pos'][1] / sizeCell)
                    selected = [x, y]
                    area[y][x] = area[y][x] + 1 if area[y][x] < 9 else 0
                    # if selected and (
                    #         x == selected[0] and y == selected[1]):  # Если нажать на фигуру в фокусе, фокус спадет
                    #     selected = []
                    # else:  # Если фокуса нет, добавляеться
                    #     selected = [x, y]
                    #     area[y][x] += 1
            screen.fill((30, 30, 30))
            draw()
            pg.display.flip()


if __name__ == '__main__':
    generationArea(sizeField, sizeField)
    main()
    pg.quit()
