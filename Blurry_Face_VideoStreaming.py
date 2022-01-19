import cv2

def algo (x):
    pass

captura = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cv2.namedWindow('frame')
cv2.createTrackbar('Blur','frame',0,15,algo)
cv2.createTrackbar('Gray','frame',0,1,algo)

while True:
    ret, frame = captura.read()
    valor = cv2.getTrackbarPos('Blur', 'frame')
    valorGris = cv2.getTrackbarPos('Gray','frame')
    if valorGris ==1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rostros = faceClassif.detectMultiScale(frame,1.3,5)

    for (x,y,w,h) in rostros:
        if valor > 0:
            frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],(valor,valor))
    
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
captura.release()
cv2.destroyAllWindows()


