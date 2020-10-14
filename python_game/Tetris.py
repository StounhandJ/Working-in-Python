import pygame as pg
import time
import random

pg.init()
screen = pg.display.set_mode((660, 660))
clock = pg.time.Clock()
area=[];
for y in range(0,20):
	area.append([]);
	for x in range(0,10):
		area[y][x]=1;
#Цвета -------------------
red=(230,20,20)
green=(20,230,20)
green_b=(10,120,10)
white=(230,230,230)
#---------------------
FONT = pg.font.Font(None, 48)


class Text:  # Объект текста
    def __init__(self):
        pass

    def draw(screen, x, y, text, color):  # 1 сцена; 2,3 позиция; 4 текст; 5 цвет
        o_text = FONT.render(text, True, color)
        text_rect = o_text.get_rect()
        text_rect.center = (x, y)
        screen.blit(o_text, text_rect)

def draw(): #Прорисовка всего поля
    for x in range(10):
        for y in range(20):
            if area[x][y] != 0:
                color = (250 - 10 * math.log2(area[x][y]), 250 - 20 * math.log2(area[x][y]), 0)
                pg.draw.rect(screen, color, (120 * x, 120 * y, 115, 115))
                Text.draw(screen, 120 * x + 60, 120 * y + 60, str(area[x][y]), green)
            else:
                pg.draw.rect(screen, white, (120 * x, 120 * y, 115, 115))

def main(): #Основное тело программы
    start=False #Активность игры
    while start:
        screen.fill((30, 30, 30))
        draw();
        for event in pg.event.get(): #Проверка соытий
            if event.type == pg.QUIT: #Событие закрытия приложения
                start = False
            elif (event.type == pg.KEYDOWN): #Нажате клавиши
                pass
        pg.display.flip() #Перерисовка сцены
        clock.tick(6) #Задержка


if __name__ == '__main__':
    main()
    pg.quit()