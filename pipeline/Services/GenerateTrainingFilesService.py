from interface import implements
from Interfaces.IGenerateTrainingFilesService import IGenerateTrainingFilesService

class GenerateTrainingFilesService(implements(IGenerateTrainingFilesService)):
    def GenerateTrainingFiles(self, imagesFolder: str):
        raise NotImplementedError