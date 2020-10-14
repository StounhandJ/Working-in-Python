import pygame as pg
print("pg")
import conf
print("conf")

pg.init()
print(1)
COLOR_INACTIVE = conf.COLOR_INACTIVE
print(2)
COLOR_ACTIVE = conf.COLOR_ACTIVE
print(3)
fault = 0
print(4)
out_text = ["", "", "error"]
print(5)
FONT = pg.font.Font("C:\Windows\{}onts\{}rial.ttf".format("f","a"), 24)
print(6)


class InputBox:  # Объект поля для ввода
    def __init__(self, x, y, w, h, text=''):  # 1,2 позиция; 3,4 размер; 5 текст
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.x = x
        self.w = w

    def handle_event(self, event, all_text):  # 1 событие на сцене; 2 текст уровня
        global out_text, fault
        itog = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                self.text += event.unicode
                if event.unicode == all_text[len(self.text) - 1]:
                    out_text[0] = all_text[:-(len(all_text) - len(self.text))]
                    out_text[1] = ""
                    out_text[2] = all_text[len(self.text):len(all_text)]
                    if all_text == self.text:
                        itog = True
                        self.text = ""
                else:
                    self.text = self.text[:-1]
                    out_text[1] = all_text[len(self.text)]
                    out_text[2] = all_text[len(self.text) + 1:len(all_text)]
                    fault += 1
            self.txt_surface = FONT.render(self.text, True, self.color)
            return itog

    def draw(self, screen):  # 1 сцена
        width = max(200,self.txt_surface.get_width() + 10)
        x = self.x - (width - self.w) / 2
        self.rect.x = x
        self.rect.w = width
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 2))
        pg.draw.rect(screen, self.color, self.rect, 2)


class OutBox:  # Объект поля для вывода
    def __init__(self, x, y, w, h, text=''):  # 1,2 позиция; 3,4 размер; 5 текст
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.color_green = (0, 255, 0)
        self.color_red = (255, 0, 0)
        self.color_oran = (255, 255, 255)
        self.text = text
        self.txt_surface = FONT.render("", True, self.color)
        self.txt_surface2 = FONT.render("", True, self.color)
        self.txt_surface3 = FONT.render("", True, self.color)
        self.x = x
        self.w = w

    def draw(self, screen):  # 1 сцена
        self.txt_surface = FONT.render(out_text[0], True, self.color_green)
        self.txt_surface2 = FONT.render(out_text[2], True, self.color_oran)
        self.txt_surface3 = FONT.render("_" if out_text[1] == ' ' else out_text[1] if out_text[1] != "" else "", True, self.color_red)
        width = max(200, self.txt_surface.get_width()+ self.txt_surface2.get_width() + self.txt_surface3.get_width()+10)
        x = self.x - (width - self.w)/2
        self.rect.x = x
        self.rect.w = width
        if out_text[1] != "":
            tes = screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 3))
            tes2 = screen.blit(self.txt_surface3, (self.rect.x + tes.w + 5, self.rect.y + 3))
            screen.blit(self.txt_surface2, (self.rect.x + tes.w + tes2.w + 5, self.rect.y + 3))
        else:
            tes = screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 3))
            screen.blit(self.txt_surface2, (self.rect.x + tes.w + 5, self.rect.y + 3))
        pg.draw.rect(screen, self.color, self.rect, 2)


class button:  # Объект кнопка
    def __init__(self,screen, x, y, w, h, t_x, t_y,
                 text=''):  # 1,2 позиция кнопки; 3,4 размер; 5,6 отступ текста от верхнего левого угла; 7 текст;
        self.screen = screen
        self.rect = pg.Rect(x, y, w, h)
        self.t_x = t_x
        self.t_y = t_y
        self.color_green = (0, 255, 0)
        self.color_red = (255, 0, 0)
        self.color_oran = (255, 255, 255)
        self.color = (0,0,0)
        self.text = text
        self.pos=False

    def draw(self,color=COLOR_INACTIVE):  # Отрисовка
        self.color=color
        pg.draw.rect(self.screen, color, self.rect, 2)  # Отрисовка прямоугольника
        pg.draw.rect(self.screen, COLOR_ACTIVE if self.pos else self.color, self.rect, 2), self.screen.blit(
            (FONT.render(self.text, True, COLOR_ACTIVE if self.pos else self.color)), (self.rect.x + self.t_x, self.rect.y + self.t_y))

    def handle_event(self, event):  # Проверка нажатия
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        elif event.type == pg.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.pos = True
            else: self.pos = False


class Text:  # Объект текста
    def __init__(self):
        pass

    def draw(screen, x, y, text, color):  # 1 сцена; 2,3 позиция; 4 текст; 5 цвет
        o_text = FONT.render(text, True, color)
        text_rect = o_text.get_rect()
        text_rect.center = (x, y)
        screen.blit(o_text, text_rect)
