import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW);
num = 0
cnt_max = [0,0]
itog = 0
sumn = 0
print("Ожидайте....")
while sumn<200:
    flag, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, 1)

    contours, h = cv2.findContours(thresh, 1, 2)

    for cnt in contours:
    	rect = cv2.minAreaRect(cnt)
    	area = int(rect[1][0] * rect[1][1])
    	if area > cnt_max[0] and area>50000:
    		cnt_max[0] = area
    		cnt_max[1] = cnt 	
    if num>10 and cnt_max[0]!=0:
    	cnt = cnt_max[1]7
    	peri = cv2.arcLength(cnt, True)
    	approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
    	if len(approx) == 3:
    		pass
    		# print("Треуголиник")
    		# cv2.drawContours(img, [cnt], 0, (240, 20, 80), 2)
    	elif len(approx) == 4:
    		itog +=1
    		# # print("Квадрат")
    		# Отоброжение на картинке
    		# rect = cv2.minAreaRect(cnt) # пытаемся вписать прямоугольник
    		# box = cv2.boxPoints(rect) # поиск четырех вершин прямоугольника
    		# box = np.int0(box) # округление координат
    		# cv2.drawContours(img,[box],0,(255,0,0),2) # рисуем прямоугольник
    	else:
    		itog-=1
    		# #print("Круг")
    		# Отоброжение на картинке
    		# ellipse = cv2.fitEllipse(cnt)
    		# cv2.ellipse(img,ellipse,(180,0,0),2)
    		# cv2.drawContours(img, [cnt], 0, (255, 180, 0), 2)
    	num = 0
    	cnt_max = [0,0]
    try:
        # cv2.imshow('img', gray)
        cv2.imshow('img', img)
        #cv2.imshow('img', thresh)
    except Exception as e:
        cap.realese()
        raise

    num+=1
    sumn+=1
    ch = cv2.waitKey(5)
    if ch == 27:
        break

if itog>0:
	print("Квадрат")
else:
	print("Круг")