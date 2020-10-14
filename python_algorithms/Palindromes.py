def check(m,i,weight): # Проверка символов на сходство m строка; i центральный символ; weight дальность сравниваемых символов от центра
	if i+weight<=len(m)-1 and i-weight>=0: # Проверка на границы строки
		if (m[i-weight]==m[i+weight]): # Сравнение символов
			return True
	return False

def palindromes(m): # Возвращает массив палиндром из строки или False
	dlin = len(m)-1 # Для удобства длинна строки в переменной
	out=[]
	for i in range(1,dlin): # Проход по всей строке
		run=True
		weight=1
		while run: # Проверка на палиндром от центрального символа, при совпадение увеличеваеться количество символов проверка на палиндром, до не совпадения
			if check(m,i,weight):
				out.append(m[i-weight:i+weight+1])
				weight+=1
			else: run=False
	return out

def controller(line,options='all'): # Необязательная функция позволяющая по options вернуть определенный палиндром
	if(options=='all'):return palindromes(line)
	if(options=='min'):return min(palindromes(line),key=len)
	if(options=='max'):return max(palindromes(line),key=len)
	return False

# ---------------------- Тест ---------------------- #

print( controller('sgkgs') )
print( controller('sgkgsjjlj','all') )
print( controller('sgkgsjjlj','min') )
print( controller('sgkgsjjlj','max') )
print( controller('sdlfa') )
print( controller('') )

"""
>['gkg', 'sgkgs']
>['gkg', 'sgkgs', 'jlj']
>gkg
>sgkgs
>[]
>[]
"""
