import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image = cv2.imread('image.png')
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(grayImage,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
for(x,y,w,h) in face:
  cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()