import cv2

def algo (x):
    pass

imagen = cv2.imread('oficina.jpeg')
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cv2.namedWindow('ventana')
cv2.createTrackbar('Blur','ventana',0,15,algo)
cv2.createTrackbar('Gris','ventana',0,1,algo)

while True:
    val = cv2.getTrackbarPos('Blur','ventana')
    valorGris = cv2.getTrackbarPos('Gris','ventana')

    if valorGris == 1:
        imagenN = cv2.cvtColor(imagen.copy(),cv2.COLOR_BGR2GRAY)
    else:
        imagenN = imagen.copy()
    rostros = faceClassif.detectMultiScale(imagen, 1.1,5)
    for (x,y,w,h) in rostros:
        if val > 0:
            imagenN[y:y+h,x:x+w] = cv2.blur(imagenN[y:y+h,x:x+w],(val,val))
    cv2.imshow('ventana', imagenN)
    k = cv2.waitKey(1)
    if k == 27:
        break
cv2.destroyAllWindows()