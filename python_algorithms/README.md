Решение разных задач на Python
=====================
***
Список:  
[Palindromes.py](https://github.com/StounhandJ/Working-in-Python/tree/master/python_algorithms#palindromespy)  
[ShareThem.py](https://github.com/StounhandJ/Working-in-Python/tree/master/python_algorithms#palindromespy)  
[KeyMes.py](https://github.com/StounhandJ/Working-in-Python/tree/master/python_algorithms#palindromespy)  
[DefiningShape.py](https://github.com/StounhandJ/Working-in-Python/tree/master/python_algorithms#palindromespy) 
---
Palindromes.py
---
[[source]](https://github.com/StounhandJ/Working-in-Python/blob/master/python_algorithms/Palindromes.py)
### Условие:
###### Формат ввода
В единственной строке входных данных записана одна строка из базы Аркадия — непустая последовательность строчных букв английского алфавита. Длина строки составляет не менее 2 и не превосходит 200000 символов.

###### Формат вывода
Выведите минимальную по длине подстроку строки из входных данных, состоящую хотя бы из двух символов и являющуюся палиндромом. Напомним, что среди всех таких строк Аркадий хочет найти лексикографически минимальную.
### Документация:  
###### controller(line,options) - возврат всех палиндромов строки с опицей в масиве: 
line(str) - Cтрока для проверки.  
options(str) - Ключ возврата, необязательный параметр: all - все палиндромы в строке; min - самый короткий палиндром в строке; max - самый длинный палиндром в строке; 
###### palindromes(m) - возврат всех палиндромов в масиве:
m(str) - Cтрока для проверки.
***
ShareThem.py
---
[[source]](https://github.com/StounhandJ/Working-in-Python/blob/master/python_algorithms/ShareThem.py)
### Условие:  
###### Формат ввода
В первой строке входных данных записано целое число  — количество мишеней. Каждая из последующих n строк содержит целое число обозначающее тип мишени. Если t1=0 то мишень является кругом и далее следуют три целых числа r,x и y определяющие радиус и координаты центра круга соответственно  Если же t1=1 то мишень является прямоугольником, который затем определяют восемь целых чисел x1,y1,x2,y2,x3,y3,x4,y4 — координаты всех четырёх вершин перечисленных в порядке обхода по часовой стрелке или против часовой стрелки. Гарантируется, что данные четыре вершины образуют прямоугольник ненулевой площади.

###### Формат вывода
Если существует прямая, которая поделит каждый из имеющихся кругов и прямоугольников на две части одинаковой площади, выведите “Yes”. В противном случае выведите “No”.
### Документация:  
###### controller(mas) - принимает масив объектов и возвращает True если объекты можно разделить или False если нет:
mas(array) - масив объектов, формат [0,радиус,x,y] для круга и [1,x1,y1,x2,y2,x3,y3,x4,y4] для прямоугольников  
###### rectangle(rectangle) - принимет масив формата прямоугольника и возвращает масив со значение удвоенного центра [1,0,x,y]:
rectangle(array) - масив прямоугольника [1,x1,y1,x2,y2,x3,y3,x4,y4]
***
KeyMes.py
---
[[source]](https://github.com/StounhandJ/Working-in-Python/blob/master/python_algorithms/KeyMes.py)
### Документация: 
###### Выводит в уведомление Windows 10 нажатые сочетания клавиш. Возврат по типу (ctrl+z+c)
DefiningShape.py
---
[[source]](https://github.com/StounhandJ/Working-in-Python/blob/master/python_algorithms/DefiningShape.py)
### Условие:  
Определяет что за объект перед камерой: квадрат, круг,(треугольник). При помощи библиотеки OpenCV.
