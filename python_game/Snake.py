import pygame as pg
import time
import random

pg.init()
screen = pg.display.set_mode((660, 660))
clock = pg.time.Clock()
pxy=20
clet=660/pxy
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

def draw_c(color,x,y):
    pg.draw.rect(screen, color, (clet * x, clet * y, clet-5, clet-5))

class food: #Объект еда
    def __init__(self): #При нициализации сразу создается
        self.x = random.randint(0, pxy-1)
        self.y = random.randint(0, pxy-1)
    def add(self): #Создание новой еды
        self.x = random.randint(0, pxy-1)
        self.y = random.randint(0, pxy-1)
    def draw(self): #Прорисовка еды
        draw_c(red,self.x,self.y)


class head(): #Объект голова
    def __init__(self):
        self.x = pxy/2
        self.y = pxy/2
        self.xt = 0
        self.yt = 0
    def event(self, ev): #Работа с событиями(нажатия)
        if ev == "w" or ev == "ц":
            self.yt = -1
            self.xt = 0
        elif ev == "s" or ev == "ы":
            self.yt = 1
            self.xt = 0
        elif ev == "d" or ev == "в":
            self.xt = 1
            self.yt = 0
        elif ev == "a" or ev == "ф":
            self.xt = -1
            self.yt = 0

    def draw(self): #Прорисовка змейки и проверка границ
        self.x += self.xt
        self.y += self.yt
        if self.x>pxy-1:
            self.x=0
        if self.x < 0:
            self.x = pxy-1
        if self.y > pxy-1:
            self.y = 0
        if self.y < 0:
            self.y = pxy-1

        draw_c(green_b,self.x,self.y)



def main(): #Основное тело программы
    done = False
    tail_m=[[10,10]]
    tail=3 #Длина хвоста
    foodn = food() #Объект еда
    snake = head() #Объект голова
    fail=False #Ошибка столкновения
    start=False #Активность игры
    while not done: #Цикл до закрытия приложения
        #Стартовая надпись
        draw_c(green_b,pxy/2,pxy/2)
        foodn.draw()
        Text.draw(screen,300,300,"Нажмите любую клавишу",white)
        for event in pg.event.get(): #Проверка соытий
            if event.type == pg.QUIT: #Событие закрытия приложения
                done = True
            elif (event.type == pg.KEYDOWN): #Нажате клавиши
                snake.yt=-1
                start=True
                tail_m.pop()
        pg.display.flip()
        clock.tick(6)
        #Сама игра
        while start:
            screen.fill((30, 30, 30))
            for event in pg.event.get(): #Проверка соытий
                if event.type == pg.QUIT: #Событие закрытия приложения
                    done = True
                    start = False
                elif (event.type == pg.KEYDOWN): #Нажате клавиши
                    snake.event(event.unicode)

            if snake.x == foodn.x and snake.y == foodn.y: #Проверка попадание головы на еду
                print('win')
                good = False
                while not good: #Проверка что бы еда не спавнилась внутри тела
                    foodn.add()
                    check=[foodn.x,foodn.y]
                    if not(check in tail_m):
                        good=True
                tail+=1 #Увелечение количества честей тела

            for t in range(len(tail_m)): #Проверка попадание головы на часть тела
                if snake.x == tail_m[t][0] and snake.y == tail_m[t][1]:
                    tail=3
                    snake.x=pxy/2
                    snake.y=pxy/2
                    snake.xt=0
                    snake.yt=0
                    fail=True #Для очистки масива тела

            while fail:  #Очистка тела
                for t in range(len(tail_m)):
                    tail_m.pop() #Удаление последнего элемента масива
                pg.display.flip()
                fail=False
                start=False #Режим игры не активен


            tail_m.append([snake.x, snake.y]) #добавление нового элемента в масив тела как ближайщего к голове
            while len(tail_m)>tail: #Удаление последнего элемента масива как лишнего учитывая длину
                tail_m.pop(0)

            foodn.draw() #Прорисовка еды
            for t in range(len(tail_m)): #Прорисовка тела
                draw_c(green,tail_m[t][0],tail_m[t][1]) #Прорисовка тела змеи

            snake.draw() #Прорисовка головы
            pg.display.flip() #Перерисовка сцены
            clock.tick(6) #Задержка


if __name__ == '__main__':
    main()
    pg.quit()