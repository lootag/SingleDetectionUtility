from injector import Injector, Binder, inject
from typing import Dict
from Interfaces.IGenerateTrainingFilesService import IGenerateTrainingFilesService
from Interfaces.IInferenceService import IInferenceService
from Interfaces.ISeparateImagesFromAnnotationsService import ISeparateImagesFromAnnotationsService
from Interfaces.ITrainingService import ITrainingService
from Services.GenerateTrainingFilesService import GenerateTrainingFilesService
from Services.InferenceService import InferenceService
from Services.SeparateImagesFromAnnotationsService import SeparteImagesFromAnnotationsService
from Services.TrainingService import TrainingService
import json

def BindServices(binder: Binder):
    binder.bind(IGenerateTrainingFilesService, to=GenerateTrainingFilesService())
    binder.bind(IInferenceService, to=InferenceService())
    binder.bind(ISeparateImagesFromAnnotationsService, to=SeparteImagesFromAnnotationsService())
    binder.bind(ITrainingService, to=TrainingService())

class Program:
    @inject
    def __init__(self, generateTrainingFilesService: IGenerateTrainingFilesService,
                 inferenceService: IInferenceService,
                 separateImagesFromAnnotationsService: ISeparateImagesFromAnnotationsService,
                 trainingService: ITrainingService):
                
                self.__generateTrainingFilesService = generateTrainingFilesService
                self.__inferenceService = inferenceService
                self.__separateImagesFromAnnotationsService = separateImagesFromAnnotationsService
                self.__trainingService = trainingService
    
    def Main(self) -> None:
        config: Dict = self.__Configure()
        self.__separateImagesFromAnnotationsService.SeparateImagesFromAnnotations(config["imagesFolder"], config["annotationsFolder"])
        self.__generateTrainingFilesService.GenerateTrainingFiles(imagesFolder = config["imagesFolder"])
        self.__trainingService.Train()
        self.__inferenceService.Predict()
    
    def __Configure(self) -> Dict:
        with open("config.json") as config:
            return json.load(config)

injector: Injector = Injector(BindServices)
program = injector.get(Program)

if __name__ == "__main__":
    program.Main()
                