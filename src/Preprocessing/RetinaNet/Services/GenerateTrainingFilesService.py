import os
import random
import math
from interface import implements
from Preprocessing.RetinaNet.Interfaces.IGenerateTrainingFilesService import IGenerateTrainingFilesService

class GenerateTrainingFilesService(implements(IGenerateTrainingFilesService)):
    def GenerateTrainingFiles(self, imagesFolder: str, mainFolder: str, valSize: float):
        self.__GenerateTrainVal(imagesFolder, mainFolder)
        self.__GenerateTrainAndVal(imagesFolder, mainFolder, valSize)
    
    def __GenerateTrainVal(self, imagesFolder: str, mainFolder: str):
        with open(os.path.join(mainFolder, "trainval.txt"), 'w') as trainval:
            for file in os.listdir(imagesFolder):
                if file[-3:] == "jpg":
                    fileName = file.replace(".jpg", "")
                    trainval.write(fileName + "\n")

    def __GenerateTrainAndVal(self, imagesFolder: str, mainFolder: str, valSize: float) -> None:
        allImages = os.listdir(imagesFolder)
        random.shuffle(allImages)
        valImages = allImages[:round(valSize*len(allImages))]
        trainImages = allImages[round(valSize*len(allImages)):]
        with open(os.path.join(mainFolder, "val.txt"), 'w') as val:
            for file in valImages:
                if file[-3:] == "jpg":
                    fileName = file.replace(".jpg", "")
                    val.write(fileName + "\n")
        
        with open(os.path.join(mainFolder, "train.txt"), 'w') as train:
            for file in trainImages:
                if file[-3:] == "jpg":
                    fileName = file.replace(".jpg", "")
                    train.write(fileName + "\n")
        
    
            
        
        

