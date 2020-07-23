from interface import Interface

class IGenerateTrainingFilesService(Interface):
    def GenerateTrainingFiles(self, imagesFolder: str):
        pass