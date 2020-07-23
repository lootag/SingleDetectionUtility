import os
from shutil import copyfile
from interface import implements
from Interfaces.ISeparateImagesFromAnnotationsService import ISeparateImagesFromAnnotationsService
from typing import *
import types

class SeparteImagesFromAnnotationsService(implements(ISeparateImagesFromAnnotationsService)):
    def SeparateImagesFromAnnotations(self, imagesFolder: str, annotationsFolder: str):
        for file in os.listdir(imagesFolder):
            if file[-3:] == "txt":
                copyfile(src = os.path.join(imagesFolder, file), dst = os.path.join(annotationsFolder, file))
                os.remove(os.path.join(imagesFolder, file))