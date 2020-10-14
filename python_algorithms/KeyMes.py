from win10toast import ToastNotifier # pip install win10toast
import keyboard as key  # pip install keyboard
import time # Стандартная библиотека

n = ToastNotifier()  # Для создание окна
start = False  # Сочетание клавиш ещё не нажато
keys = []  # Масив нажатых символов
button = ['ctrl','alt','fn'] # Массив клавишь активаций


def out(end): # Вывод конечного сообщения
    s = '' # Строка вывода
    for x in end: # Добавление всех клавишь из масива в строку
        s += x + "+"
    n.show_toast("Нажато сочетание", s[0:-1], duration=5) # Вывод уведомление, время действия 5сек
    time.sleep(2) # Ожидание, для защиты от блокировки Windows


def check(name): # Обработка нажатий
    global start, keys
    if start: # Если сочетание активно то True
        if name.event_type == "up" and name.name in button: # Проверка на отжатие клавиши
            if len(keys)>1: out(keys) # Отправить итог нажатий
            keys = [] # Сброс настроек
            start = False
        elif name.event_type == "down" and keys[len(keys) - 1] != name.name: # Если была нажата клавиша и её не было раньше, добавить в масив
            keys.append(name.name)
    else: 
        if name.event_type == "down" and name.name in button: # Если зажата одна из клавишь активаций, добавить её и начать считывание следующих
            start = True
            keys.append(name.name)


while True: # Бесконечный цикл
    pres = key.read_event(check) # Запись нажатых клавишь
    if pres: check(pres) # Если нажата клавиша отправить на проверку

