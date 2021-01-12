import pygame as pg
import Chess
import config

area = config.areaMain
pg.init()
screen = pg.display.set_mode((1000, 760))
clock = pg.time.Clock()
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
turn = 1  # Очеред игрока
AllMoves = []  # Все возможные хода для фигуры в фокусе
selected = []  # Координаты фигуры в фокусе
log = []  # Лог ходов
eventGame = ""  # Событие в игре


class Text:  # Объект текста
    @staticmethod
    def draw(window, x, y, text, color, sizeFont):  # 1 сцена; 2,3 позиция; 4 текст; 5 цвет
        """Отрисовка текста в определенном месте сцены.


        :param window: Сцена
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
        window.blit(o_text, text_rect)


def addLog(text, player):
    """Добавляет событие в лог действий

    :param text: Текст события
    :param player: Игрок сделавший событие
    """
    log.append([text, player])
    if len(log) > 30:
        log.pop(0)


def controlerClick(oldX, oldY, newX, newY):
    """Управление фигурой.

    :param oldX: Позиция фигуры сейчас по X
    :param oldY: Позиция фигуры сейчас по Y
    :param newX: Новая позиция для фигуры по X
    :param newY: Новая позиция для фигуры по Y
    """
    global eventGame, area
    for mas in area:  # По старым координатам находим фигуру и получем все данные для создания объекта и управление им
        if mas["coordinates"][0] == oldX and mas["coordinates"][1] == oldY:
            figure = eval(f'Chess.{mas["chessPiece"]}')(oldX, oldY, mas["player"], area)
            res = figure.move(newX, newY)
            area = figure.Area.area
            eventGame = figure.Area.event
            return res


def draw():
    """Отрисовка всего поля

    """
    screen.fill(0)
    count = 1
    for x in range(8):  # Отрисовка клеток
        for y in range(8):

            if count % 2 == 0:
                pg.draw.rect(screen, (70, 50, 0), (95 * x, 95 * y, 90, 90))
            else:
                pg.draw.rect(screen, (200, 150, 20), (95 * x, 95 * y, 90, 90))
            count += 1
        count = 0 if count == 9 else 1

    for mas in AllMoves:
        pg.draw.rect(screen, (230, 255, 0), (95 * mas[0], 760 - 95 * mas[1] - 95, 90, 90))

    for mas in area:  # Добавляем изоображения фигур
        x = mas["coordinates"][0]
        y = mas["coordinates"][1]
        image = pg.image.load(f'img/{mas["chessPiece"]}{mas["player"]}.png').convert_alpha()
        screen.blit(image, (95 * x, 760 - 95 * y - 95))

    if selected:  # Рисуем заленый квадрат фокуса для фигуры, если он есть
        pg.draw.rect(screen, (40, 250, 0), (95 * selected[0], 760 - 95 * selected[1] - 95, 90, 90), 5)

    Text.draw(screen, 880, 50, eventGame, (230, 20, 20), 40)  # Текст события
    Text.draw(screen, 880, 100, f'Ход {"белых" if turn == 1 else "черных"}', (230, 20, 20), 50)  # Текст, чей ход
    count = 0
    for var in log:  # Текст, лог действий
        Text.draw(screen, 880, 150 + count * 20, var[0], (10, 120, 10) if var[1] == 1 else (20, 230, 20), 20)
        count += 1

    pg.display.flip()  # Перерисовка сцены
    clock.tick(200)  # Задержка


def main():
    """Главная функция для работы Шахмат

    """
    global selected, turn, log, AllMoves
    done = False
    while not done:
        for event in pg.event.get():  # Проверка соытий
            if event.type == pg.QUIT:  # Событие закрытия приложения
                done = True

            elif event.type == pg.MOUSEBUTTONDOWN:  # Нажате клавиши

                if event.dict['button'] == 3:  # Если правая кнопка, то убрать фокус на фигуре
                    selected = []
                else:
                    x = int(event.dict['pos'][0] / 95)
                    y = 7 - int(event.dict['pos'][1] / 95)
                    if selected and (
                            x == selected[0] and y == selected[1]):  # Если нажать на фигуру в фокусе, фокус спадет
                        selected = []
                        AllMoves = []
                    elif selected:  # Если фигура в фокусе и нажатие в любое место, попытка хода
                        if controlerClick(selected[0], selected[1], x, y):
                            addLog(
                                f'{"Белый" if turn == 1 else "Черный"} с {names[selected[0]]}{selected[1] + 1} на {names[x]}{y + 1}',
                                turn)
                            turn = 1 if turn == 2 else 2
                            selected = []
                            AllMoves = []
                    else:  # Если фокуса нет, добавляеться
                        for mas in area:
                            if mas["coordinates"][0] == x and mas["coordinates"][1] == y and mas["player"] == turn:
                                figure = eval(f'Chess.{mas["chessPiece"]}')(x, y, mas["player"], area)
                                AllMoves = figure.getPossibleMoves()
                                selected = [x, y]
                                break
            draw()  # Запуск прорисовки поля


if __name__ == '__main__':
    main()
    pg.quit()
