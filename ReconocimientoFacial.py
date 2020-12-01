import cv2
import os

#PROGRAMA PARA DETECCIÓN DE CUBREBOCAS

dataPath = 'Data' #Carpeta en donde se almacenan las imagenes de la BD
imagePaths = os.listdir(dataPath)
#print(imagePaths)

#Método de OpenCV para reconocimeinto de rostros
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Lectura del modelo donde se almacenan las etiquetas
face_recognizer.read('modeloLBPHFace.xml')

#Captura de la cámara web
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Método de OpenCV para la detección de objetos en video
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

#Detección de rostro
while True:	
	ret,frame = cap.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = face_recognizer.predict(rostro)

		cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
		
		#Se comparan las etiquetas del xml para saber de que clase se trata
		if result[0] ==0:
			cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		else:
			cv2.putText(frame,'Sin cubrebocas',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		
	cv2.imshow('Deteccion de cubrebocas',frame)
	k = cv2.waitKey(1)
	if k == 27:
		break

	

cap.release()
cv2.destroyAllWindows()


