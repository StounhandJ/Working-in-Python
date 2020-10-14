import pygame as pg
import random 
import math
area = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 2, 0]] #Поле
dlin=3 #количество элементов
storona=dlin  #0 сдвиг вправо; dlina слвиг влево
pg.init()
screen = pg.display.set_mode((480, 480)) #Размер окна
clock = pg.time.Clock()
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
    for x in range(4):
        for y in range(4):
            if area[x][y] != 0:
                color = (250 - 10 * math.log2(area[x][y]), 250 - 20 * math.log2(area[x][y]), 0)
                pg.draw.rect(screen, color, (120 * x, 120 * y, 115, 115))
                Text.draw(screen, 120 * x + 60, 120 * y + 60, str(area[x][y]), green)
            else:
                pg.draw.rect(screen, white, (120 * x, 120 * y, 115, 115))
    pg.display.flip()  # Перерисовка сцены
    clock.tick(200)  # Задержка

def reda(mas): #работа с масивом
    good = False
    while not good:
        col = mas.count(0)  # узнаем количество 0
        redact = 0 #Количество сложений
        for t in range(col): #удаляем все 0
            mas.remove(0)
        for t in range(col): #добавляем нужно количество в заданую сторону
            mas.insert(storona,0)
        draw()
        for t in range(storona, 0 if storona==dlin else dlin,-1 if storona==dlin else 1): #складывание чисел
            tg=t-1 if storona==dlin else t+1 #В зависимости от строноны действия
            if mas[t]==mas[tg] and mas[t]!=0: #Проерка на одинаковые числа
                mas[tg]=mas[t]*2
                mas[t]=0
                redact+=1
        if redact == 0 :
            good = True
    return mas

def rand_con(): #Добавляет двойку в игру
    global area
    good = False
    sum=0
    for t in range(len(area)):
        sum=sum+area[t].count(0)
    if sum==0: #Проверка на наличие нулей
        area=[[0,0,0,0],[0,0,0,0],[0,0,2,0],[0,0,2,0]]
    else:
        while not good: #До тех пор пока 2 не встанет в пустую позицию
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if area[x][y]==0: #Проыерка на занятость ячейки
                area[x][y]=2
                good=True

def right_left(): #Движение вправо или лево
    global area
    mirror=[]
    for col in range(len(area[0])): #Создаем копию масива
       for t in range(4):
          mirror.append(area[t][col])
       mirror=reda(mirror) #редактируем копию
       for t in range(4): #возвращаем копию в оригинал
           area[t][col]=mirror[t]
       mirror=[]
    rand_con()

def top_down(): #Движение вверх или вниз
  global area
  mirror = []
  for col in range(len(area)): #Создаем копию масива
    for t in range(len(area[col])):
       mirror.append(area[col][t])
    mirror=reda(mirror) #редактируем копию
    for t in range(4): #возвращаем копию в оригинал
       area[col][t]=mirror[t]
    mirror=[]
  rand_con()

def controler(ev): #Котролер нажатий, ставит сторону и направление
    global storona
    if ev == "w" or ev == "ц":
        storona=dlin
        print('w')
        top_down()
    elif ev == "s" or ev == "ы":
        storona=0
        top_down()
    elif ev == "d" or ev == "в":
        storona = 0
        right_left()
    elif ev == "a" or ev == "ф":
        storona=dlin
        right_left()

def main(): #основное тело программы
    down=False
    while not down:
        for event in pg.event.get(): #Проверка соытий
            if event.type == pg.QUIT: #Событие закрытия приложения
                down = True
            elif (event.type == pg.KEYDOWN): #Нажате клавиши
                controler(event.unicode)
            draw()


if __name__ == '__main__':
    main()
    pg.quit()
