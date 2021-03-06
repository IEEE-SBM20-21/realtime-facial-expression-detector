import cv2
import os

#change directory for different expressions
currentDirectory = "D:/Facial Expression Detector/training_images_expressions/surprised/"
classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
                    
images = os.listdir(currentDirectory)
i = 1

for img in images:
    image = currentDirectory + img
    print(str(i))

    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = classifier.detectMultiScale(img)
    
    for face in faces:
        x, y, w, h = [ v for v in face ]
        roi_face = img[y:y+h, x:x+w]
        roi_face = cv2.resize(roi_face, (300, 300), interpolation = cv2.INTER_AREA)
        
        file = image.split('/')
        file = file[-1]

        cv2.imwrite(file, roi_face)
        print(file + " Saved")
        i += 1
    
cv2.destroyAllWindows()


images = os.listdir(currentDirectory)
i = 1
    
for filename in os.listdir(currentDirectory): 
    dst = str(i) + ".jpg"
    src = currentDirectory + filename 
    dst = currentDirectory + dst 
    
    os.rename(src, dst) 
    i += 1
    
cv2.destroyAllWindows()