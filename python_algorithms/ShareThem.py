def rectangle(rectangle): # Преобразование прямоугольника в стандарт [тип,int,x,y] где x и y координаты центра фигуры
	return [1,0,rectangle[1]+rectangle[5],rectangle[2]+rectangle[6]]

def controller(mas): # Основная функция проверяющая все фигуры на нахождение их на одной прямой
	if len(mas)<3: return True # Если объектов меньше 3, то они 100% находяться на одной прямой

	try: # Если фигура прямоугольник, у него ищеться удвоенная середина и она задаеться в новом формате для дальнейшей проверки
		for i in range(0,len(mas)):
			if mas[i][0]==1: mas[i]=rectangle(mas[i]) 
	except Exception as e:
		return "Ошибка. Неверные данные для прямоугольника"

	try: # Проверка всех объектов типа [тип,int,x,y] где x и y координаты центров фигур. Проверка при помощи формулы <векторного произведения для 3 точек>
		for i in range(0,len(mas)-2):
			if (((mas[i][2]-mas[i+2][2])*(mas[i+1][3]-mas[i+2][3]))-((mas[i+1][2]-mas[i+2][2])*(mas[i][3]-mas[i+2][3]))!=0): return False
	except Exception as e:
		return "Ошибка проверки"

	return True


# ---------------------- Тест ---------------------- #
# На вход даёться масив по типу: [[0,радиус1,x1,y1],[0,радиус2,x2,y2],[0,радиус3,x3,y3]] для круга
#                                [[1,x1,y1,x2,y2,x3,y3,x4,y4]] для прямоугольников
# Даёться ответ можно ли разрезать эти все фигуры по полам одной прямой
print(controller([[0,1,2,2],[0,2,0,0],[0,3,-6,-6],[1,4,3,3,3,3,4,4,4]]))
print(controller([[0,1,2,2],[0,2,0,0],[0,3,-6,-6],[1,4,3,3,3,3,4,4,4]]))
print(controller([[0,3,6,9],[0,1,2,6],[0,5,4,9]]))
print(controller([[0,6,1,1],[0,8,4,4],[0,2,2,2]]))
print(controller([[1,1,2,3,4,5,6,7,8],[1,3,3,6,3,6,5,3,5]]))
"""
>True
>True
>False
>True
>True
"""
# ---------------------- Наработки ---------------------- #







"""
# Код для ввода данных (думаю не нужен тут)
figure = []
for i in range(0,int(input("Количество фигур: "))):
	typ = int(input("Тип фигуры(0-круг;1-прямоугольник): "))
	if typ==0:
		figure.append([typ,int(input('Радиус:')),int(input('X:')),int(input('Y:'))])
	elif typ==1:
		inp=input('4 точки по координатам XY: ')
		figure.append([int(inp[i]) for i in range(0,len(inp)-1)])
"""
