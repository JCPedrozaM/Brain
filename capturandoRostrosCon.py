import cv2
import os
import imutils
from datetime import datetime

#PROGRAMA QUE CAPTURA ROSTROS CON CUBREBOCAS

personName = "Con cubrebocas" #Nombre de la etiqueta
dataPath = "Data" #Carpeta en donde se almacenan las imagenes capturadas
personPath = dataPath + "/" + personName

#Se crea la carpeta de la etiqueta en caso de que no exista
if not os.path.exists(personPath):
	print("Carpeta creada: ",personPath)
	os.makedirs(personPath)

#Se activa la cámara web
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Método de OpenCV para la detección de objetos en video
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
count = 0

#Detección de rostro
while True:

	ret, frame = cap.read()
	if ret == False: break
	frame =  imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)
#Almacenamiento de imagenes en la ruta correspondiente
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
		now = datetime.now()
		now = str(now.day) + "_" + str(now.month) + "_" + str(now.year) + "_" + str(now.hour) + "_" + str(now.minute) + "_" + str(now.second)
		cv2.imwrite(personPath + "/rostro_"+now+".jpg",rostro)
		count = count + 1
	cv2.imshow("Captura rostros con cubrebocas",frame)

	k =  cv2.waitKey(1)
	if k == 27 or count >= 300:
		break

cap.release()
cv2.destroyAllWindows()
