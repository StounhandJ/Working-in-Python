import pygame as pg

print("pg")
import time

print("time")
import conf

print("conf")
import object1

print("obj")
import os

print("os")
import requests

print(0)
pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = conf.COLOR_INACTIVE
COLOR_ACTIVE = conf.COLOR_ACTIVE
COLOR_RED = conf.COLOR_RED
COLOR_GREEN = conf.COLOR_GREEN
FONT = pg.font.Font("C:\Windows\{}onts\{}rial.ttf".format("f", "a"), 48)
out_text = ["", "", "error"]
fault = 0
all_text1 = {
    1: {1: "аа оо ао оа оо ао аа", 2: "аоо оао оаа аао аоа", 3: "вв лл вл лв лв вл лл", 4: "вал лав вла алв аал"},
    2: {1: "ыы дд ыд ды да вд оы", 2: "вад выд дао лав вал", 3: "дыв ала доы лва двы", 4: "дыва вода алов выл"},
    3: {1: "фф жж фж жф фа жа дф", 2: "жол дол ыфо дыл лаф", 3: "пп рр рп рп рр пр", 4: "пар пож рыв дар жол"},
    4: {1: "кг гк кк гг кг гк гг", 2: "кга гва вак даг рак", 3: "уш шу уу шш шу уш", 4: "душ лук ыдл ваш гул"},
    5: {1: "цщ щщ цщ щц цщ щщ цц", 2: "цол кол щад дыш фол", 3: "щук лык кло щог квд", 4: "ука фаш дуу щал вал"},
    6: {1: "мм тт мт тм мм тт мт", 2: "там тут мол выл дул", 3: "руд мог кап рат фут", 4: "вал тор мар дыл кол"},
    7: {1: "ен нн ее не не ее нн", 2: "реп нет вел нол выл", 3: "ии пи ри ии ви ли ии", 4: "пир вил дел нет пар"},
    8: {1: "сс ьь ьс сь ьс сь сс", 2: "сел фел цнь жил дел", 3: "лок про цун лук миг", 4: "тел аль жел шов кул"},
    9: {1: "чч бб чб бч бб чч бч", 2: "чаб лаб бол чат век", 3: "жаб кра лыч ибь сыт", 4: "фаб баф тик рим лес"},
    10: {1: "йй зз зй зй йй зй зз", 2: "зел пйл сел был жил", 3: "ран зил дыв биг нип", 4: "жаг лаж бат оль риц"},
    11: {1: "хх ээ хэ эх хх эх ээ", 2: "эло хэл лек хит шик", 3: "лока выше лучш холе", 4: "дыка пика экла сень"},
    12: {1: "яю юю яя юю яю юя яя", 2: "юлат жила пеки якрк", 3: "ликъ бик чек век дар", 4: "жак вак дюл яды вид"},
    13: {1: "пар лоук вил жфл кль", 2: "река вода тень бень", 3: "лень фарк баки чеки", 4: "жало холо чэло цеши"},
    14: {1: "рало тень бари пари", 2: "якорь вепрь жалос вер", 3: "букв фадю эдун вели", 4: "нет ыфе нар шан жал"},
    15: {1: "дом был тут давно", 2: "нет ничего сейчас тут", 3: "только ветер дует", 4: "конец пришёл уже"}}
completed_lvl = conf.completed_lvl
average_speed = conf.data['average_speed']
average_speed_col = conf.data['average_speed_col']
time_min = conf.data['time_min']
print(1)
try:
    out = open("icon.png", "wb")
    out.write(requests.get("https://www.zap.md/sites/default/files/acme-aula-dragon-deep.png").content)
    out.close()
    pg.display.set_icon(pg.image.load("icon.png"))
    os.remove("icon.png")
except IOError:
    pass
pg.display.set_caption('Слепая печать')
print(2)


def lok():
    pass


def close():
    conf.data['average_speed'] = average_speed
    conf.data['average_speed_col'] = average_speed_col
    conf.data['time_min'] = time_min
    conf.completed_lvl = completed_lvl
    conf.creat()


def main(num):  # Сцена уровня
    global out_text, fault, completed_lvl, average_speed, average_speed_col, time_min, lvl_col
    if not (num in all_text1):
        done = True
        res = False
    else:
        clock = pg.time.Clock()
        all_text = all_text1[num]
        lvl = 1
        out_box1 = object1.OutBox(200, 150, 225, 32, text=all_text[1])
        object1.out_text[2] = all_text[1]
        input_box1 = object1.InputBox(200, 250, 225, 32)
        back = object1.button(screen, 0, 449, 90, 30, 12, 3, "Назад")
        done = False
        start_ticks = pg.time.get_ticks()
        out_box1.draw(screen)
    while not done:
        screen.fill((30, 30, 30))
        seconds = (pg.time.get_ticks() - start_ticks) / 1000
        input_box1.draw(screen)
        back.draw()
        object1.Text.draw(screen, 215, 140, ("{}:{}".format(int(seconds / 60), int(seconds) % 60)), COLOR_ACTIVE)
        object1.Text.draw(screen, 370, 140, ("Ошибок {}".format(str(object1.fault))), COLOR_ACTIVE)
        for event in pg.event.get():
            out_box1.draw(screen)
            if event.type == pg.QUIT:
                done = True
                res = False
                screen.fill((30, 30, 30))
            elif input_box1.handle_event(event, all_text[lvl]):
                lvl += 1
                if lvl > len(all_text):
                    screen.fill((30, 30, 30))
                    average_speed_col += 1
                    hop = int(((len(all_text[1]) + len(all_text[2])) / int(seconds)) * 60)
                    average_speed = (average_speed + hop) / average_speed_col
                    time_min += seconds / 60
                    object1.Text.draw(screen, 320, 120, ('Этап пройден :) {} символов в минуту'.format(hop)),
                                      COLOR_ACTIVE)
                    pg.display.flip()
                    time.sleep(2)
                    done = True
                    res = True
                    completed_lvl[num - 1] = True
                else:
                    object1.out_text[0] = ""
                    object1.out_text[2] = all_text[lvl]
            elif back.handle_event(event):
                done = True
                res = True
                object1.out_text[0] = ""
                object1.out_text[1] = ""
                object1.out_text[2] = ""
                object1.fault = 0
            pg.display.flip()
        clock.tick(30)
    start() if res else close()


def prof():  # Сцена профиля
    global average_speed, average_speed_col, time_min, completed_lvl
    clock = pg.time.Clock()
    done = False
    back = object1.button(screen, 0, 444, 105, 35, 14, 5, "Назад")
    throw = object1.button(screen, 23, 120, 115, 35, 3, 5, "Сбросить")
    while not done:
        screen.fill((30, 30, 30))
        for event in pg.event.get():
            back.draw()
            throw.draw()
            object1.Text.draw(screen, 265, 40, ("Среднее количество символов в минуту: {}".format(average_speed)),
                              COLOR_GREEN)
            object1.Text.draw(screen, 155, 80, ("Время обучения {0:.1f} мин.".format(time_min)), COLOR_GREEN)
            if event.type == pg.QUIT:  # Проверка на выход из программы
                done = True
                screen.fill((30, 30, 30))
                close()
            elif (event.type == pg.MOUSEBUTTONDOWN) or (event.type == pg.MOUSEMOTION):  # Проверка нажатия мыши
                if back.handle_event(event):  # Назад
                    done = True
                    start()
                elif throw.handle_event(event):  # Сбросить
                    average_speed_col = 0
                    average_speed = 0.0
                    time_min = 0
                    for i in range(len(completed_lvl)): completed_lvl[i] = False
            pg.display.flip()  # Перерисовка всего
        clock.tick(50)  # Время обновления


def start():  # Стартовая сцена
    clock = pg.time.Clock()
    done = False  # Переменная активности сцены
    rect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # Создание кнопок уровней
    y = 0
    for i in range(len(rect)):  # Создание кнопок уровней
        x = (i % 5) * 120
        y += 0 if i % 5 != 0 else 70
        rect[i] = object1.button(screen, 20 + x, -50 + y, 100, 50, 20, 15, "LvL {}".format(str(i + 1)))
    rect_prof = object1.button(screen, 260, 400, 110, 35, 3, 5, "Профиль")  # Создание кнопки профиля
    while not done:
        screen.fill((30, 30, 30))
        rect_prof.draw()  # Отрисовка кнопки профиля
        for i in range(len(rect)):  # Отрисовка кнопок уровней
            if completed_lvl[i]:
                rect[i].draw(COLOR_GREEN)
            else:
                rect[i].draw(COLOR_RED)
        for event in pg.event.get():  # Получения события
            if event.type == pg.QUIT:  # Проверка на выход из программы
                done = True
                screen.fill((30, 30, 30))
                close()
            elif (event.type == pg.MOUSEBUTTONDOWN) or (event.type == pg.MOUSEMOTION):  # Проверка нажатия мыши
                for i in range(len(rect)):  # На уровни
                    if rect[i].handle_event(event):  # При совпадение запуск main с передачей номера уровня
                        main(i + 1)
                        rect[i].draw(COLOR_GREEN if completed_lvl[i] else COLOR_RED)
                        done = True
                if rect_prof.handle_event(event):  # На профиль
                    done = True
                    prof()
            pg.display.flip()  # Перерисовка всего
        clock.tick(50)  # Время обновления


if __name__ == '__main__':
    for i in range(10):
        screen.fill((30, 30, 30))
        object1.Text.draw(screen, 540, 460, "by StounhandJ", (30, 30, 230 - i * 20))

        o_text = FONT.render("Слепая печать", True, (30, 30, 230 - i * 20))
        text_rect = o_text.get_rect()
        text_rect.center = (300, 220)
        screen.blit(o_text, text_rect)

        pg.display.flip()
        time.sleep(0.15)
    # star=object.button(screen,240,200,90,30,5,5,"Начать")
    # star.draw()
    # pg.display.flip()
    start()
    pg.quit()
