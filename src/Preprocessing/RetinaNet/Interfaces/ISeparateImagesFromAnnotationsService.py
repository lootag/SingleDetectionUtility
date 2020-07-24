from interface import Interface

class ISeparateImagesFromAnnotationsService(Interface):
    def SeparateImagesFromAnnotations(self, imagesFolder: str, annotationsFolder: str):
        pass