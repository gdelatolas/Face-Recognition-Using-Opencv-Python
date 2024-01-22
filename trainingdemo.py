import cv2
import numpy as np
from PIL import Image
import os



recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'datasets'

def getImageID(path):
    
    # load all images (f) from dataset
    # imagePath is a list of the images
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for imagePath in imagePaths:
        faceImage = Image.open(imagePath).convert('L')
        faceNP = np.array(faceImage, 'uint8')
        Id = os.path.split(imagePath)[-1].split(".")[1]
        Id = int(Id)

        faces.append(faceNP)
        ids.append(Id)
        cv2.imshow("Training", faceNP)
        cv2.waitKey(1)
    return ids, faces

IDs, facedata = getImageID(path)
recognizer.train(facedata, np.array(IDs))
recognizer.write("Trainer.yml")
cv2.destroyAllWindows()
print("Training Completed...")