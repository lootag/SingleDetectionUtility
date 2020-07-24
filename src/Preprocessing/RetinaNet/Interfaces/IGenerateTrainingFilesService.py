from interface import Interface

class IGenerateTrainingFilesService(Interface):
    def GenerateTrainingFiles(self, imagesFolder: str, mainFolder: str, valSize: float):
        pass