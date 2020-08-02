import sys
import os
from shutil import copyfile
from interface import implements
from typing import *
import types
from Preprocessing.RetinaNet.Interfaces.ISeparateImagesFromAnnotationsService import ISeparateImagesFromAnnotationsService

class SeparteImagesFromAnnotationsService(implements(ISeparateImagesFromAnnotationsService)):
    def SeparateImagesFromAnnotations(self, imagesFolder: str, annotationsFolder: str):
        self.__EliminateSpacesFromFileNames(imagesFolder = imagesFolder)
        for file in os.listdir(imagesFolder):
            if file[-3:] == "xml":
                copyfile(src = os.path.join(imagesFolder, file), dst = os.path.join(annotationsFolder, file))
                os.remove(os.path.join(imagesFolder, file))
    
    def __EliminateSpacesFromFileNames(self, imagesFolder: str):
        for file in os.listdir(imagesFolder):
            if " " in file:
                newFileName = file.replace(" ", "")
                os.rename(src = os.path.join(imagesFolder, file), dst = os.path.join(imagesFolder, newFileName))

        